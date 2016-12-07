import os
import zipfile

def generateStudentList(submissionsPath):
    ''' returns list of all student names in directory'''
    students = set()
    for f in os.listdir(submissionsPath):
        if '_' in f:
            name = f[:f.index('_')]
            students.add(name)
        else:
            students.add(f)

    return students

def organizeSubmissions(submissionsPath, students):
    ''' creates folders in the directory submissionsPath for each student'''
    for student in students:
        studentFolder = submissionsPath + '/' + student
        if not os.path.exists(studentFolder):
            os.mkdir(studentFolder)
        for f in os.listdir(submissionsPath):
            if 'zip' in f and student in f:
                unzip_submission(submissionsPath + '/' + f, studentFolder)
            if len(f) > len(student) and student in f:
                os.rename(submissionsPath + '/' + f, studentFolder + '/' + f)
        print('fuuuuck')
        renameAllFiles(studentFolder, ['client', 'server', 'makefile'])

def renameAllFiles(studentFolder, names):
    ''' normalizes names and gets rid of camino naming conventions '''
    print('Renaming files in: ' + studentFolder)
    for f in os.listdir(studentFolder):
        for name in names:
            if name in f:
                os.rename(studentFolder + '/' + f, studentFolder + '/' + f[f.rfind('_')+1:])

def unzip_submission(path, name):
    zip_ref = zipfile.ZipFile(path, 'r')
    zip_ref.extractall(name)
    zip_ref.close()

if __name__ == '__main__':
    students = generateStudentList(os.getcwd() + '/friday')
    organizeSubmissions(os.getcwd() + '/friday', students)
