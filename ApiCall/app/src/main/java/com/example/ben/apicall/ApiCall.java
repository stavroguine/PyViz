package com.example.ben.apicall;

import android.os.AsyncTask;
import android.util.Log;
import android.widget.Toast;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class ApiCall extends AsyncTask<Object, Void, JSONObject> {

    private Exception exception;
    HttpURLConnection urlConnection;

    JSONObject jsonResponse = null;
    @Override
    protected JSONObject  doInBackground(Object... params) {
        StringBuilder result = new StringBuilder();
        //connexion à l'api et buffer du json
        try {
            URL url = new URL("http://192.168.0.19:1440/youplaboum");
            urlConnection = (HttpURLConnection) url.openConnection();
            InputStream in = new BufferedInputStream(urlConnection.getInputStream());
            Log.e("lol", "ici");
            BufferedReader reader = new BufferedReader(new InputStreamReader(in));
            String line;

            while ((line = reader.readLine()) != null) {

                result.append(line);
            }
            jsonResponse = new JSONObject(result.toString());

        }catch( Exception e) {
            e.printStackTrace();
        }
        finally {
            urlConnection.disconnect();
        }
        return jsonResponse;
    }


}
