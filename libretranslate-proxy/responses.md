# Example Responses


```
#
# upper sorbian container: DE -> HSB
#

curl -X POST -H "Content-Type: application/json" -d '{
  "source_language": "de",
  "target_language": "hsb",
  "text": "Guten Tag"
}' http://localhost:25000/translate
{"marked_input":[["Guten Tag"]],"marked_translation":[["Dobry d\u017ae\u0144"]],"model":"witaj_jc_de_hsb_2024-08-09","unks":[]}


#
# upper sorbian container: HSB -> DE
#

curl -X POST -H "Content-Type: application/json" -d '{
  "source_language": "hsb",
  "target_language": "de",
  "text": "Witaj k nam"
}' http://localhost:25000/translate
{"marked_input":[["Witaj k nam"]],"marked_translation":[["Hallo zu uns"]],"model":"witaj_jc_hsb_de_2024-07-31","unks":[]}


#
# libretranslate container: DE -> EN
#

curl -X POST http://0.0.0.0:5000/translate -H "Content-Type: application/json" -d '{"q": "Wie gehts?", "source": "de", "target": "en"}'
{"translatedText":"How are you?"}

```


