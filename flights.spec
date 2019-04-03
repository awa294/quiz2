Parameters:
        Payment:
                show in money. [property Money]
                show in miles. [property Miles]

        Money or Miles: 
		[if Money]
			[!Miles]
		[else]
			[Miles]
		[if Miles]
			[!Money]
		[else]
			[Money]
	

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
	
	BF or CF:
		[if BFselected]
			[!CFselected]
		[else]
			[CFselected]
		[if CFselected]
			[!BFselected]
		[else]
			[BFselected]
	
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

	Flexible Dates:
		selected. 	[property FDselected]	
		not selected. 

	Options Flexible Dates:
		Flexible Days. [if FDselected] [FDayselected]
		5 Weeks.       [if FDselected] [5Wselected]

	FDay or 5W:
		[if FDayselected]
			[!5Wselected]
		[else]
			[5Wselected]
		[if 5Wselected]
			[!FDayselected]
		[else]
			[FDayselected]

	Delta Only:
		selected. 	[property DOselected]
		not selected.

	Delta Partner Airlines:
		selected. 	[property DPAselected]
		not selected.

 	DO or DPA:
		[if DOselected]
			[!DPAselected]
		[else]
			[DPAselected]
		[if DPAselected]
			[!DOselected]
		[else]
			[DOselected]

