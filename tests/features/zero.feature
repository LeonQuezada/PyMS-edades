Feature: Devuelve mensaje por edad dado
	como usuario del sistema eades
	quien usuarios del sistema
	quiero ingresar una edad y me regreso.

    Scenario: con edad mayor a -1
		dado que ingreso la edad "-1"
		cuando consulto mi mensaje
		entoces ve que "no existes"

		Scenario: con edad mayor a 12 pero mayor a -1
		dado que ingreso la edad "8"
		cuando consulto mi mensaje
		entoces ve que "eres niño"
