package com.globant;
import java.util.ArrayList;

public class BowlingGame {
    public static int getScore(ArrayList<Integer> line)
    {
        Integer score = 0;
        for( Integer i : line)
        {
            score += i;
        }
        return score;
    }
}