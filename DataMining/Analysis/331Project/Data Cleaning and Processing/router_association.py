import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder


def preprocess(df):
    """
    Apply one hot encoding and create a hash table from location -> index.

    Returns
        Tuple:
            [0] - processed data frame
            [1] - Hash Table mapping Locations to Indices
            [2] - Hash Table mapping BSSID to Indixes
    """
    transformed = []
    df_mod = df.copy()
    router_map = {name: n for n, name in enumerate(df_mod['BSSID'].unique())}
    location_map = {name: n for n, name in enumerate(df_mod['Location'].unique())}

    df_mod['Location'] = df_mod['Location'].replace(location_map)
    df_mod['BSSID'] = df_mod["BSSID"].replace(router_map)

    enc = OneHotEncoder(categorical_features=[2])
    enc.fit(df_mod)

    processed = pd.DataFrame(data=enc.transform(df_mod).toarray())

    return (processed, location_map, router_map)

def encode_target(df, target_column):
    """Add Labels to the dataset."""
    df_mod = df.copy()
    targets = df_mod[target_column].unique()
    map_to_int = {name: n for n, name in enumerate(targets)}
    df_mod["Target"] = df_mod[target_column].replace(map_to_int)

    return (df_mod, targets)

def get_code(tree, feature_names, target_names,
             spacer_base="    "):
    """Produce psuedo-code for decision tree. http://stackoverflow.com/a/30104792."""
    left      = tree.tree_.children_left
    right     = tree.tree_.children_right
    threshold = tree.tree_.threshold
    features  = [feature_names[i] for i in tree.tree_.feature]
    value = tree.tree_.value

    def recurse(left, right, threshold, features, node, depth):
        spacer = spacer_base * depth
        if (threshold[node] != -2):
            print(spacer + "if ( " + str(features[node]) + " <= " + \
                  str(threshold[node]) + " ) {")
            if left[node] != -1:
                    recurse(left, right, threshold, features,
                            left[node], depth+1)
            print(spacer + "}\n" + spacer +"else {")
            if right[node] != -1:
                    recurse(left, right, threshold, features,
                            right[node], depth+1)
            print(spacer + "}")
        else:
            target = value[node]
            for i, v in zip(np.nonzero(target)[1],
                            target[np.nonzero(target)]):
                target_name = target_names[i]
                target_count = int(v)
                print(spacer + "return " + str(target_name) + \
                      " ( " + str(target_count) + " examples )")

    recurse(left, right, threshold, features, 0, 0)

def routers_multiple_associations(df):
    """Print the number of routers total and the number which are associated with multiple access points."""
    routers = df['BSSID'].unique()
    border_routers = []
    for router in routers:
        associated_aps = df[df['BSSID'] == router]['Location'].unique()
        if len (associated_aps) > 1:
            border_routers.append(router)

    print(len(routers))
    print(len(border_routers))

def get_accuracy(file_name):
    counter = 0
    with open(file_name, 'r') as f:
        content = f.readlines()
        correct = [c.strip().lower() for c in content[0].split(',')]
        predictions = [c.strip().lower() for c in content[1].split(',')]

        for i in range(len(correct)):
            if correct[i] != predictions[i]:
                counter += 1

    return (counter/len(predictions))

def main(percentage):
    """Given a percentage for splitting the dataset, fit the training set and apply the rest as a test set."""
    df = pd.read_csv('cellStrength.log')
    df.drop('SSID', 1, inplace=True)
    processed = preprocess(df)
    location_col = processed[0].shape[1]-4

    hash_to_location = {y:x for x,y in processed[1].items()}

    df2, targets = encode_target(processed[0], location_col)
    msk = np.random.rand(len(df)) < percentage
    test = df2[~msk].copy()
    train = df2[msk].copy()

    open('golden.csv', 'w').write(','.join([hash_to_location[p] for p in test['Target'].tolist()]) + '\n' )

    test.drop(186, 1, inplace=True)
    test.drop('Target', 1, inplace=True)

    features = list(df2.columns[:location_col]) + list(df2.columns[location_col+1:-1])

    y = train['Target']
    X = train[features]

    dt = DecisionTreeClassifier(min_samples_split=3, random_state=99)
    try:
        dt.fit(X, y)
    except ValueError:
        return
    predictions = dt.predict(test).tolist()
    open('golden.csv', 'a').write(','.join([hash_to_location[p] for p in predictions]))

    # get_code(dt, features, targets)
    return get_accuracy('golden.csv')

if __name__ == '__main__':
    # df = pd.read_csv('cellStrength.log')
    # routers_multiple_associations(df)
    accuracies = {}

    for i in np.arange(0,1,0.1):
        accuracies[i] = []
        for j in range(10):
            accuracies[i].append(main(i))

    print(accuracies)
