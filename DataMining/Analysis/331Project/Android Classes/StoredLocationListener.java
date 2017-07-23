package com.example.armanelahi.rssi_mapper;

import android.content.Context;
import android.location.Location;
import android.location.LocationListener;
import android.os.Bundle;

/**
 * Created by Arman Elahi on 3/21/2017.
 */

/*---------- Listener class to get coordinates ------------- */
public class StoredLocationListener implements LocationListener {

    private String latitude;
    private String longitude;

    @Override
    public void onLocationChanged(Location loc) {
        this.longitude = Double.toString(loc.getLongitude());
        this.latitude = Double.toString(loc.getLatitude());
    }

    @Override
    public void onProviderDisabled(String provider) {}

    @Override
    public void onProviderEnabled(String provider) {}

    @Override
    public void onStatusChanged(String provider, int status, Bundle extras) {}

    public String getLocation(){
        return this.latitude + "," + this.longitude;
    }
}