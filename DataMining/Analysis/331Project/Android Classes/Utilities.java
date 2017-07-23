package com.example.armanelahi.rssi_mapper;

import android.content.Context;
import android.os.Environment;
import android.widget.Toast;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.OutputStreamWriter;

/**
 * Created by Arman Elahi on 3/18/2017.
 */

public class Utilities {
    public static void writeToLog(Context context, String filename, String message){
        String path = context.getExternalFilesDir(Environment.getDataDirectory().getAbsolutePath()).getAbsolutePath();
        try{
            FileOutputStream fos = new FileOutputStream(new File(path + "/" + filename), true);
            fos.write(message.getBytes());
            Toast.makeText(context, "Wrote to file.", Toast.LENGTH_SHORT).show();
            fos.flush();
            fos.close();

        } catch (Exception e){
            Toast.makeText(context, "Could not write to file", Toast.LENGTH_SHORT).show();
        }

    }

    public boolean isExternalStorageWritable() {
        String state = Environment.getExternalStorageState();
        if (Environment.MEDIA_MOUNTED.equals(state)) {
            return true;
        }
        return false;
    }
}
