package com.example.armanelahi.rssi_mapper;

import android.Manifest;
import android.content.Context;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.net.wifi.ScanResult;
import android.net.wifi.WifiInfo;
import android.net.wifi.WifiManager;
import android.os.Build;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v4.app.ActivityCompat;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.ButtonBarLayout;
import android.support.v7.widget.Toolbar;
import android.telephony.CellInfo;
import android.telephony.CellInfoGsm;
import android.telephony.CellInfoLte;
import android.telephony.CellSignalStrengthGsm;
import android.telephony.PhoneStateListener;
import android.telephony.SignalStrength;
import android.telephony.TelephonyManager;
import android.util.Log;
import android.view.View;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.List;

public class RSSILocatorActivity extends AppCompatActivity {

    private FileOutputStream fos;
    private EditText locationEditText;
    private TextView outputTextView;
    private Button button;
    private WifiManager wm;
    private PhoneStateListener pl;
    private SignalStrength signal;
    int PERMISSION_ALL = 1;
    TelephonyManager telephonyManager;
    LocationManager lm;
    StoredLocationListener ll;
    private Context ctx;

    String[] PERMISSIONS = {Manifest.permission.CHANGE_WIFI_STATE,
            Manifest.permission.READ_PHONE_STATE,
            Manifest.permission.ACCESS_COARSE_LOCATION,
            Manifest.permission.ACCESS_FINE_LOCATION,
            Manifest.permission.ACCESS_WIFI_STATE};


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_rssilocator);

        button = (Button) findViewById(R.id.new_entry_button);
        locationEditText = (EditText) findViewById(R.id.location_tag);
        outputTextView = (TextView) findViewById(R.id.output_text_view);

        ctx = this;
        button.setOnClickListener(onClickListener);

        if (!hasPermissions(this, PERMISSIONS)) {
            ActivityCompat.requestPermissions(this, PERMISSIONS, PERMISSION_ALL);
        }

        wm = (WifiManager) getSystemService(Context.WIFI_SERVICE);

        pl = new PhoneStateListener() {
            public void onSignalStrengthsChanged(SignalStrength ss) {
                signal = ss;
            }
        };

        telephonyManager = (TelephonyManager) this.getSystemService(Context.TELEPHONY_SERVICE);
        telephonyManager.listen(pl, PhoneStateListener.LISTEN_SIGNAL_STRENGTHS);
        lm = (LocationManager) getSystemService(Context.LOCATION_SERVICE);
        ll = new StoredLocationListener();
        if (ActivityCompat.checkSelfPermission(ctx, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission(ctx, Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            return;
        } else {
            lm.requestLocationUpdates(LocationManager.GPS_PROVIDER, 5000, 10, ll);
        }
    }

    private View.OnClickListener onClickListener = new View.OnClickListener() {

        @Override
        public void onClick(final View v) {

//            String loc = locationEditText.getText().toString();

            String cellStrength = "";
            cellStrength += ll.getLocation();

            List<CellInfo> cellInfos = telephonyManager.getAllCellInfo();
            WifiInfo info = wm.getConnectionInfo();
            cellStrength += ((CellInfoLte) cellInfos.get(0)).getCellSignalStrength().getDbm() + ",";
            cellStrength += info.getBSSID() + "," + info.getSSID() + "," + info.getRssi() + "," + info.getLinkSpeed();
            cellStrength += "\n";

            outputTextView.setText(cellStrength);
            Utilities.writeToLog(ctx, "signals.log", cellStrength);
        }
    };

    @Override
    public void onRequestPermissionsResult(int requestCode,
                                           String permissions[], int[] grantResults) {
      return;
    }

    public static boolean hasPermissions(Context context, String... permissions) {
        if (android.os.Build.VERSION.SDK_INT >= Build.VERSION_CODES.M && context != null && permissions != null) {
            for (String permission : permissions) {
                if (ActivityCompat.checkSelfPermission(context, permission) != PackageManager.PERMISSION_GRANTED) {
                    return false;
                }
            }
        }
        return true;
    }
}

