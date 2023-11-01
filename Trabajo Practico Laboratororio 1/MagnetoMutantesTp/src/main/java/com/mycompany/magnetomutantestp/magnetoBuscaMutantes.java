/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.magnetomutantestp;

import java.util.Scanner;

/**
 *
 * @author Nahuel
 */
public class magnetoBuscaMutantes {
    public static boolean isMutant(String[] dna) {
        int n = dna.length;
        if (n == 0 || n != dna[0].length()) {
            return false; // Ve que no este vacia
        }

        int count = 0; //Contador de Coincidencias Mutantes

        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                char currentChar = dna[i].charAt(j);
                
                // For para verificar de manera horizontal
                if (j + 3 < n &&
                    currentChar == dna[i].charAt(j + 1) &&
                    currentChar == dna[i].charAt(j + 2) &&
                    currentChar == dna[i].charAt(j + 3)) {
                    count++;
                }

                // For para verificar verticalmente
                if (i + 3 < n &&
                    currentChar == dna[i + 1].charAt(j) &&
                    currentChar == dna[i + 2].charAt(j) &&
                    currentChar == dna[i + 3].charAt(j)) {
                    count++;
                }

                // Si ya encontramos más de una coincidencia se retorna  True
                if (count > 1) {
                    return true;
                }
            }
        }

        // For para verificar pero de manera diagonal normal y su inversa.
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                char currentChar = dna[i].charAt(j);
                
                // Diagonal Normal
                if (i + 3 < n && j + 3 < n &&
                    currentChar == dna[i + 1].charAt(j + 1) &&
                    currentChar == dna[i + 2].charAt(j + 2) &&
                    currentChar == dna[i + 3].charAt(j + 3)) {
                    count++;
                }

                //Inversa
                if (i + 3 < n && j - 3 >= 0 &&
                    currentChar == dna[i + 1].charAt(j - 1) &&
                    currentChar == dna[i + 2].charAt(j - 2) &&
                    currentChar == dna[i + 3].charAt(j - 3)) {
                    count++;
                }

                // Al igual que arriba si hay coincidencia mutante se retorna True
                if (count > 1) {
                    return true;
                }
            }
        }

        return false; //Si no hay coincidencias False :(
    }
    
    
    //Comprueba que las letras ingresadas sean (A,T,C,G)
     public static boolean isValidDNA(String[] dna) {
        for (String row : dna) {
            if (!row.matches("[ATCG]+")) {
                return false;
            }
        }
        return true;
    }
    
    

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] dna = new String[6];
        
       //Solicita que llenemos las filas pero comprueba que las condiciones sean correctas:
        System.out.println("Ingresa las filas de la matriz de ADN (6 filas):");
        for (int i = 0; i < 6; i++) {
            System.out.print("Ingresa la fila " + (i + 1) + ": ");
            String input = scanner.nextLine();
            
            if (input.matches("[ATCG]+")) {
                dna[i] = input;
            } else {
                System.out.println("La fila no es valida.(Recuerda solo se permiten las letras A, T, C, G).");
                i--;
            }
        }
        
        if (isValidDNA(dna)) {
            boolean isMutant = isMutant(dna);
            if (isMutant) {
                System.out.println("Es un mutante.");
            } else {
                System.out.println("No es un mutante.");
            }
        } else {
            System.out.println("La matriz de ADN ingresada no es correcta.");
        }
    }
}