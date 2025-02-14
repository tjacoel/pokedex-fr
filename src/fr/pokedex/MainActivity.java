package fr.pokedex;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Window;
import fr.pokedex.data.DataHolder;

/*
 * TODO:
 * v3.0
 * / Ajouter lien entre Pt�ra et Mega-Pt�ra
 * / Ajouter images pour les formes alternatives
 * / Evolutions disparues
 * / Clavier qui apparait quand on ferme les details d'un talent / change de langue
 * / Corriger les images de types anglais
 * / Trier les types par ordre alphab�tique dans la langue s�lectionn�e
 * 
 * ? Erreurs diverses
 * ? Layout de l'affichage des d�tails (certains mots sortent tel: Y530 (hwY530-U00))
 * 
 * v3.1
 * - Espagol
 * - Portugais
 * - Allemand
 * 
 * - Recherche par texte pur (incluant par num�ro)
 * - Theme sombre
 * - Liste des attaques apprises
 * X Recherche par type
 */

public class MainActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE);

        DataHolder.initialize(this);

        Intent intent = new Intent(this, PokemonPage.class);
        startActivity(intent);
        finish();
    }
}
