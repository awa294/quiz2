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

	MEETING EVENT CODE:
		acd34. 		
		abcde. 		
		12345. 
		1. 		[error]
		123456. 	[error]
		abcdefg. 	[error]	

	Show Best Fares For: 
		selected.	[property BFselected] 
		not selected. 

	Fare Class:
		selected. 	[if Money] [property FCselected]
		not selected. 	[if Money] [if BFselected]
	
	Options Fare Class:
		Basic Economy E (or higher).  [if FCselected]
		Main Cabin V (or higher).     [if FCselected]
		Main Cabin X (or higher).     [if FCselected]
		Main Cabin T (or higher).     [if FCselected]

	
	Options Show Best Fares For:
		Basic Economy. 	[if BFselected]
	 	Main Cabin. 	[if BFselected]
		Delta comfort+	[if BFselected]
		First Class	[if BFselected]
		Premium Select	[if BFselected]
		Delta One	[if BFselected]
	
