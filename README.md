how to use:
decompress minecraft jar for client(can be even fabric/...),get assets/textures/ ,paste to this project folder,
change folder name in combineAll.py(end with '/' ).

get material list with this code:
```java

import org.bukkit.Material;
public class Main {
    public static void main(String[] args) {
        for (Material m:Material.values()){
            System.out.print(m.name() + "|");
        }
    }
}
```
copy and paste output to "materialsFromSpigotAPI1214.html"(or whatever you like,but remember to change it in "combineAll.py")
delete "|" at the end of string,save,run combineAll.py