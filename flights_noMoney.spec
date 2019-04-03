Parameters:
        Payment:
                show in money. 
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
                selected.       
                not selected.   

	Fare Class:
		Basic Economy E (or higher).
		Main Cabin V (or higher).
		Main Cabin X (or higher). 
		Main Cabin T (or higher). 

	MEETING EVENT CODE:
		[if !5] 	[property invalid]
		[else]		[property valid]
		
