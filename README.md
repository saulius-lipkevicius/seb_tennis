# seb_tennis

0. atsidaryk `command propmt`. nueik i savo folderio lokacija su `cd` komanda. pvz `cd Desktop/seb-bot/`. ir paleisk komanda uintaliuoti packagus reikalingus - `pip install -r requirements.txt`.
1. Nueini i linka `https://book.sebarena.lt/?_ga=2.117973065.1966334876.1713010607-2100705733.1713010607#/rezervuoti/tenisas`
2. pasirenki savo filtrus, t.y. `SEB arena` ir `60 min` ir nukopini puslapio linka. 
3. iklijuoji linka i `server.py` `url` kintamaji. Tuo paciu nustatai tau tinkamus `min` ir `max` laikus bei dienas.

Galutinis zingsnis, kuri kartosi kiekviena karta perjungus pc, t.y. paleidziant bota kartu su nauja diena. nueini i folderi ir double-clickini pythono scipta `server.py`. tai iskvies serveri, kuris tau kartotinai kvies scraperi ir rades bent viena nauja laika ismes notification apacioj kairej ekrane su laiku. Jeigu netycia isjungtum notification, gali ji rasti log'e `seen_values.log`. Ji gali atsidaryti kaip text faila ir matyti visus nuscreipintus, tau tinkamus laikus. Naujausi rasti turetu buti pacioj apacioj.