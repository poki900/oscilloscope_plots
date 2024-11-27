# ----------- POL -----------
Program służy do generowania wykresów w formie plików graficznych z plików .csv. Pliki .csv zawierają pomiary z oscyloskopu. Program analizuje dane, znajduje w każdym wykresie 5 pików (zarówno minimum jak i maksimum), zaznacza je na wykresie, a następnie zapisuje wykresy do plików .png, a dane wyjściowe do pliku .csv.
Program działa w sposób automatyczny dla wszystkich plików, które wykryje w folderze data - nie ma potrzeby definiowania plików.
Program generuje poprawne piki i dane w 100% przypadków dla plików różnych od NULL (przetestowano na 194 różnorodnych przypadkach). Średni czas dla pojedynczego pliku to 360ms.

INSTRUKCJA:
1. Przygotowanie do użycia programu:
	- Jeśli pierwszy raz używasz tego programu na swoim komputerze: otwórz skrypt first_time_win klikając na niego dwukrotnie
	- Folder data służy do załadowania plików z danym w postaci plików .csv. Wyniki pojawią się w folderze results.
	- Upewnij się że twoje dane są zapisane w poniższej formie:

		x-axis,1
		second,Volt
		1.869750000000e+000,-5.07763e+001
		1.869843750000e+000,-5.07763e+001
		...

2. Uruchom program klikając dwukrotnie na skrypt run
3. Wyniki są dostępne w folderze results

# ----------- ENG -----------
The program is used to generate graphs in the form of image files from CSV files. CSV files contain measurements from the oscilloscope. The program analyzes the data, finds 5 peaks in each graph (both minimum and maximum), marks them on the plot, and then saves the graphs to PNG files, and the output to the CSV file.
The program works automatically for all files that it detects in the data folder - there is no need to define files.
The program generates correct peaks and data in 100% of cases for files different from NULL (tested on 194 different cases). The average time for a single file is 360ms.

MANUA:
1. Preparing for generating plots:
	- If you open this program for the first time on your computer You need to use the first_time_win script (double-click on it)
	- There are two directories: data and results. Put your data in a .csv file in the data directory. The results will be saved in the results directory.
	- Make sure your data are saved as an example:

		x-axis,1
		second,Volt
		1.869750000000e+000,-5.07763e+001
		1.869843750000e+000,-5.07763e+001
		...

2. Open the program by double-clicking on the script run.
3. All results are in the results directory.

# Contact
Author: Igor Szumny

Contact: igor@szumny.net