Parameters:
        Payment:
                show in money. [property Money]
                show in miles. [property Miles]

        From:
                LEX.
                SDF.
                invalid departure.        [error]

        To:
                DAB.
                EWR.
                ATL.
                invalid arrival.        [error]

        Number of Passengers:
                10.          
		0.		[error]

        Refundable Flights:
                selected.       [if Money]
                not selected.   [if Money]

	Show Best Fares For: 
		selected. 
		not selected. 

	Fare Class:
		selected. 	[if Money] [property selected]
		not selected. 	[if Money]
	
	Fare Class:
		Basic Economy E (or higher).
		Main Cabin V (or higher).
		Main Cabin X (or higher). 
		Main Cabin T (or higher). 

	
	Options Show Best Fares For:
		Basic Economy. 	[if selected]
	 	Main Cabin. 	[if selected]
		Delta comfort+	[if selected]
		First Class	[if selected]
		Premium Select	[if selected]
		Delta One	[if selected]
	
