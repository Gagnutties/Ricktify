



function RickItUp(){
    let Str = document.getElementById("EpisodeInput").value;
    let Hld = "";
    let char = 0;


    while(char<Str.length){
        if(Str[char]=="R" || Str[char]=="r"){
            Hld += Str[char];
            char++;
            while(Str[char]=="a" 
                || Str[char]=="e"
                || Str[char]=="i"
                || Str[char]=="o"
                || Str[char]=="u"
                || Str[char]=="A"
                || Str[char]=="E"
                || Str[char]=="I"
                || Str[char]=="O"
                || Str[char]=="U"){
                Hld += Str[char];
                char++;
            }
            Hld += Str[char];
            Str = Str.replace(Hld, "rick");
            Hld = "";
        }
        if(Str[char]=="M" || Str[char]=="r"){
            Hld += Str[char];
            char++;
            while(Str[char]=="a" 
                || Str[char]=="e"
                || Str[char]=="i"
                || Str[char]=="o"
                || Str[char]=="u"
                || Str[char]=="A"
                || Str[char]=="E"
                || Str[char]=="I"
                || Str[char]=="O"
                || Str[char]=="U"){
                Hld += Str[char];
                char++;
            }
            Hld += Str[char];
            Str = Str.replace(Hld, "mort");
            Hld = "";
        }
        char++;
    }
    console.log(Str);
    document.getElementById("Ricktified").innerHTML = Str;
    document.getElementById("Ricktified").style.display = "block";
}