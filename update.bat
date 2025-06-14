@echo off
REM Get timestamp
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YY=%dt:~2,2%" & set "YYYY=%dt:~0,4%" & set "MM=%dt:~4,2%" & set "DD=%dt:~6,2%"
set "HH=%dt:~8,2%" & set "Min=%dt:~10,2%" & set "Sec=%dt:~12,2%"

set "fullstamp=%YYYY%-%MM%-%DD%_%HH%-%Min%-%Sec%"
echo fullstamp: "%fullstamp%"

REM Copy the specific .ino.bin file
set "BIN_SOURCE=C:\Users\royal\Documents\Arduino\0_Projetos\Placa_Ju_OTA\build\esp32.esp32.esp32da"
copy /Y "%BIN_SOURCE%\Placa_Ju_OTA.ino.bin" .

REM Git commit & push
git add --all
git commit -m "%fullstamp%"
git push

REM Run the Python update script
python3 update.py
