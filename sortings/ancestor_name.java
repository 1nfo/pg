import java.util.*;

class anscestor_name {
    private static Map<Character, Integer> map;
    static {
        map = new HashMap<>();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
    }
    public static void sortNames(String[] names) {
        List<String[]> parsedNames = new ArrayList<>(names.length);
        for(String name: names){
            String[] tokens = name.split(" ");
            String fullName = tokens[0];
            int number = 0;
            char[] chars = tokens[1].toCharArray();
            for(int i = 0; i < chars.length ; i++ ) {
                if (i + 1 < chars.length && map.get(chars[i]) < map.get(chars[i+1])) {
                    number -= map.get(chars[i]);
                } else {
                    number += map.get(chars[i]);
                }
            }
            parsedNames.add(new String[]{fullName, String.valueOf(number), name});
        }

        Collections.sort(parsedNames, (a, b) -> {
            int result = a[0].compareTo(b[0]);
            if (result == 0) {
                result = a[1].compareTo(b[1]);
            }
            return result;
        });

        for (String[] parsedName: parsedNames) {
            System.out.println(parsedName[2]);
        }      
    }

    public static void main(String [] args){
        sortNames(new String[]{"Steven XL", "Steven XVI", "David IX", "Mary XV", "Mary XIII", "Mary XX"});
    }
}