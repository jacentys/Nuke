Schemat działania denoiser-a na nuke
Jeśli zmienił się plik na wejściu
	Odczytaj informację o pliku
	Podziel ścieżkę na składowe
	Wyszukaj numeracji i nazwy layer
	Pobierz numerację pod shotNo
	Przypisz polu ShotNo zmienną shotNo
	Przypisz polu ShotLayer zmienną shotLayer
	Jeśli pole ścieżki jest puste
		Przypisz polu sciezka pierwszy katalog w ścieżce
