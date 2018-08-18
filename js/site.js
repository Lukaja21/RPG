function processCharacter(files) {
  var character_file = files[0];
  var reader = new FileReader();
  reader.readAsText(character_file, "UTF-8");
  reader.onload = function(evt) {
    var character = JSON.parse(evt.target.result);
    try {
      document.getElementsByName("name")[0].value = character["name"];
      document.getElementsByName("xp")[0].value = character["xp"];
      document.getElementsByName("lvl")[0].value = character["lvl"];
      document.getElementsByName("coins")[0].value = character["coins"];
      document.getElementsByName("right")[0].value = character["right"];
      document.getElementsByName("left")[0].value = character["left"];
      document.getElementsByName("helmet")[0].value = character["chest"];
      document.getElementsByName("chest")[0].value = character["chest"];
      document.getElementsByName("legs")[0].value = character["legs"];
      document.getElementsByName("footwear")[0].value = character["footwear"];
      document.getElementsByName("strength")[0].value = character["strength"];
      document.getElementsByName("defense")[0].value = character["defense"];
      document.getElementsByName("speed")[0].value = character["speed"];
      document.getElementsByName("mana")[0].value = character["mana"];
      document.getElementsByName("hp")[0].value = character["hp"];
      document.getElementsByName("dexterity")[0].value = character["dexterity"];
    }
    catch (e) {
      console.log(e);

  }
}
function NPC(){
  var Influence = ["Worldwide","Nationwide","Citywide","Only immediate friends and family","Only immediate friends and family","Only friends and family","Only immediate friends and family","Only immediate friends and family","Only immediate friends and famiimmediate friends and family","Only immediate friends and family","Only immediate friends and family","Only immediate frfamily","Only immediate friends and family","Only immediate friends and family","Only immediate friends and family","Only immediatand family","Only immediate friends and family","None","Only immediate friends and family","Only immediate friends and famiimmediate friends and family","Only immediate friends and family","Only immediate friends and family","Only immediate frfamily","Only immediate friends and family","Only immediate friends and family","Only immediate friends and family","Only immediatand family","Only immediate friends and family","Only immediate friends and family","Only immediate friends and family","Only friends and family","Only immediate friends and family","Only immediate friends and family","Only immediate friends and famiimmediate friends and family","Only immediate friends and family","Only immediate friends and family","Only immediate frfamily","Only immediate friends and family","Only immediate friends and family","Only immediate friends and family"];
  var Intelligence = ["Genius","Intelligent","Average","Average","Average","Dumb","Imbecile"];
  var Manners = ["Polite","Neutral","Neutral","Neutral","Rude","Hateful","Benign"];
  var Physical_Strength = ["Strong","Athletic","Average","Average","Average","Weak","Feeble"]
  var Race = ["Elf","Dwarf","Merfolk","Human","Halfling","Goblin","Half-orc","Ent"];
  var Religious = ["True", "False"];
  var Social_Ranking = ["Prestigious","Upper Class","Middle Class","Lower Class","Serf"]
  var Wealth = ["Wealthy!","Rich","Rich","Rich","Average","Average","Average","Average","Average","Average","Average","Average","Average","Average","Average","Average","Average","Average","Average","Average","Average","Average","Average","Average","Average","Average","Average","Average","Average","Average","Average","Average","Average","Average","Poor","Poor","Poor","Poor","Poor","Poor","PoorPoor","Poor","Poor","Poor","Poor","Poor","Poor","Poor","Poor","Poor"]
  document.getElementById("NPC").innerHTML = "NPC:\nInfluence: " + Influence[Math.floor(Math.random() * Influence.length)] + "\nInte" + Intelligence[Math.floor(Math.random() * Intelligence.length)] + "\nManners: " + Manners[Math.floor(Math.random() * Manners.l"\nPhysical Strength: " + Physical_Strength[Math.floor(Math.random() * Physical_Strength.length)] + "\nRace: " + Race[MMath.random() * Race.length)] + "\nReligious" + Religious[Math.floor(Math.random() * Religious.length)] + "\nSocial RanSocial_Ranking[Math.floor(Math.random() * Social_Ranking.length)] + "\nWealth" + Wealth[Math.floor(Math.random() * Wealth.length)]
}
function saveCharacter(){
  var data = {"name":document.getElementsByName("name")[0].value, "xp":document.getElementsByName("xp")["lvl":document.getElementsByName("lvl")[0].value, "coins":document.getElementsByName("coins")["right":document.getElementsByName("right")[0].value, "left":document.getElementsByName("left")["helmet":document.getElementsByName("helmet")[0].value, "chest":document.getElementsByName("chest")["legs":document.getElementsByName("legs")[0].value, "footwear":document.getElementsByName("footwear")["strength":document.getElementsByName("strength")[0].value, "defense":document.getElementsByName("defense")["speed":document.getElementsByName("speed")[0].value, "mana":document.getElementsByName("mana")["hp":document.getElementsByName("hp")[0].value, "dexterity":document.getElementsByName("dexterity")[0].value}
  var json = JSON.stringify(data, null, 2);
  var blob = new Blob([json], {type: "application/json"});
  var url  = URL.createObjectU
  var a = document.getElementById("save");
  a.download    = "character.json";
  a.href        = url;  
}