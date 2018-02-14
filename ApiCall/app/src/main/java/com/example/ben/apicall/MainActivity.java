package com.example.ben.apicall;

import android.graphics.Color;
import android.support.constraint.ConstraintLayout;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import java.util.concurrent.ExecutionException;

import android.view.Gravity;
import android.widget.LinearLayout;
import android.widget.TextView;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class MainActivity extends AppCompatActivity  {

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

       LinearLayout layout= findViewById(R.id.layout);

        //instance de la classe ApiCall
        ApiCall task = new ApiCall();
        JSONObject result = null;
        try {
            result = task.execute().get();
            JSONArray jsonArray = result.getJSONArray("postes");
            for(int i=0; i < jsonArray.length(); i++) {
                //on r&cupère les valeurs de chaque objet json
                String commune = jsonArray.getJSONObject(i).getString("commune");
                String occurrence = jsonArray.getJSONObject(i).getString("occurrence");

                //on génère une textview pour chaque ensemble clé + valeur
                TextView textCommune = new TextView(this);
                TextView textOccurrence = new TextView(this);

                textCommune.setText("Commune : " + commune);
                textCommune.setTextSize(16);
                textCommune.setTextColor(Color.parseColor("#445EE8"));
                textCommune.setGravity(Gravity.LEFT);

                textOccurrence.setText("Occurrence : " + occurrence);
                textOccurrence.setTextSize(16);
                textOccurrence.setTextColor(Color.parseColor("#FF1E0D"));
                textOccurrence.setGravity(Gravity.RIGHT);

                layout.addView(textCommune);
                layout.addView(textOccurrence);
            }
        } catch (InterruptedException | ExecutionException | JSONException e) {
            e.printStackTrace();
        }
    }
}
