import matplotlib.pyplot as plt
from adjacency_list_graph import AdjacencyListGraph
from dijkstra import dijkstra
#3 imports from the provided code libary that allow thos code to creat graphs with points and distences,
#provide a built in dijkstra algorithm function and allow us to create a histogram

vertices = ['Harrow & Wealdstone', 'Chalfont & Latimer', 'Chesham', 'Amersham', 'Chorleywood', 'Rickmansworth',
            'Kenton', 'Moor Park', 'Watford', 'Croxley', 'West Harrow', 'Harrow-on-the-Hill', 'North Harrow',
            'Pinner', 'Northwood Hills', 'Northwood', 'Northwick Park', 'Preston Road', 'South Kenton',
            'North Wembley', 'Wembley Central', 'Stonebridge Park', 'Harlesden', 'Willesden Junction',
            'Kensal Green', "Queen's Park", 'Kilburn Park', 'Maida Vale', 'Warwick Avenue', 'Paddington',
            'Edgware Road', 'Marylebone', 'Baker Street', "Regent's Park", 'Oxford Circus', 'Piccadilly Circus',
            'Charing Cross', 'Embankment', 'Waterloo', 'Lambeth North', 'Elephant & Castle', 'Epping',
            'Theydon Bois', 'Debden', 'Loughton', 'Buckhurst Hill', 'Woodford', 'South Woodford', 'Snaresbrook',
            'Roding Valley', 'Chigwell', 'Grange Hill', 'Hainault', 'Fairlop', 'Barkingside', 'Newbury Park',
            'Gants Hill', 'Redbridge', 'Wanstead', 'Leytonstone', 'Leyton', 'Stratford', 'Mile End',
            'Bethnal Green', 'Liverpool Street', 'Bank', "St. Paul's", 'Chancery Lane', 'Holborn', 'Tottenham',
            'Bond Street', 'Marble Arch', 'Lancaster Gate', 'Queensway', 'Notting Hill Gate', 'Holland Park',
            "Shepherd's Bush", 'White City', 'East Acton', 'North Acton', 'West Acton', 'Ealing Broadway',
            'Hanger Lane', 'Perivale', 'Greenford', 'Northolt', 'South Ruislip', 'Ruislip Gardens',
            'West Ruislip', 'Bayswater', 'High Street Kensington', 'Gloucester Road', 'South Kensington',
            'Sloane Square', 'Victoria', "St. James's Park", 'Westminster', 'Temple', 'Blackfriars',
            'Mansion House', 'Cannon Street', 'Monument', 'Tower Hill', 'Aldgate', 'Moorgate', 'Barbican',
            'Farringdon', "King's Cross St. Pancras", 'Euston Square', 'Great Portland Street', 'Royal Oak',
            'Westbourne Park', 'Ladbroke Grove', 'Latimer Road', 'Wood Lane', "Shepherd's Bush Market",
            'Goldhawk Road', 'Hammersmith', 'Upminster', 'Upminster Bridge', 'Hornchurch', 'Elm Park',
            'Dagenham East', 'Dagenham Heathway', 'Becontree', 'Upney', 'Barking', 'East Ham',
            'Upton Park', 'Plaistow', 'West Ham', 'Bromley-by-Bow', 'Bow Road', 'Stepney Green',
            'Whitechapel', 'Aldgate East', "Earl's Court", 'Kensington (Olympia)', 'West Brompton',
            'Fulham Broadway', 'Parsons Green', 'Putney Bridge', 'East Putney', 'Southfields', 'Wimbledon Park',
            'Wimbledon', 'West Kensington', 'Barons Court', 'Ravenscourt Park', 'Stamford Brook', 'Turnham Green',
            'Gunnersbury', 'Kew Gardens', 'Richmond', 'Chiswick Park', 'Acton Town', 'Ealing Common', 'Stanmore',
            'Canons Park', 'Queensbury', 'Kingsbury', 'Wembley Park', 'Neasden', 'Dollis Hill', 'Willesden Green',
            'Kilburn', 'West Hampstead', 'Finchley Road', 'Swiss Cottage', "St. John's Wood", 'Green Park',
            'Southwark', 'London Bridge', 'Bermondsey', 'Canada Water', 'Canary Wharf', 'North Greenwich',
            'Canning Town', 'High Barnet', 'Totteridge & Whetstone', 'Woodside Park', 'West Finchley',
            'Mill Hill East', 'Finchley Central', 'East Finchley', 'Highgate', 'Archway', 'Tufnell Park',
            'Kentish Town', 'Edgware', 'Burnt Oak', 'Colindale', 'Hendon Central', 'Brent Cross', 'Golders Green',
            'Hampstead', 'Belsize Park', 'Chalk Farm', 'Camden Town', 'Mornington Crescent', 'Warren Street',
            'Goodge Street', 'Tottenham Court Road', 'Leicester Square', 'Euston', 'Angel', 'Old Street',
            'Borough', 'Kennington', 'Oval', 'Clapham North', 'Clapham Common', 'Clapham South', 'Balham',
            'Tooting Bec', 'Tooting Broadway', 'Colliers Wood', 'South Wimbledon', 'Morden', 'Cockfosters',
            'Oakwood', 'Southgate', 'Arnos Grove', 'Bounds Green', 'Wood Green', 'Turnpike Lane', 'Manor House',
            'Finsbury Park Victoria', 'Arsenal', 'Holloway Road', 'Caledonian Road', 'Russell Square',
            'Holborn Central', 'Covent Garden', 'Hyde Park Corner', 'Knightsbridge', 'South Ealing',
            'Northfields', 'Boston Manor', 'Osterley', 'Hounslow East', 'Hounslow Central', 'Hounslow West',
            'Hatton Cross', 'Heathrow Terminals 1, 2, 3', 'Heathrow Terminal 5', 'Heathrow Terminal 4',
            'North Ealing', 'Park Royal', 'Alperton', 'Sudbury Town', 'Sudbury Hill', 'South Harrow',
            'Rayners Lane', 'Eastcote', 'Ruislip Manor', 'Ruislip', 'Ickenham', 'Hillingdon', 'Uxbridge',
            'Walthamstow Central', 'Blackhorse Road', 'Tottenham Hale', 'Seven Sisters', 'Finsbury Park',
            'Highbury & Islington', 'Pimlico', 'Vauxhall', 'Stockwell', 'Brixton','Nine Elms',
            'Battersea Power Station']
#vertices is defining each point on the graph we are going to make for this code, in this ccase it would be the
#station names


edges = [('Harrow & Wealdstone', 'Kenton', 2, 1), ('Kenton', 'South Kenton', 2, 1), ('South Kenton', 'North Wembley', 2, 1), ('North Wembley', 'Wembley Central', 2, 1), ('Wembley Central', 'Stonebridge Park', 2, 1),
         ('Stonebridge Park', 'Harlesden', 2, 1), ('Harlesden', 'Willesden Junction', 2, 1), ('Willesden Junction', 'Kensal Green', 3, 1), ('Kensal Green', "Queen's Park", 2, 1), ("Queen's Park", 'Kilburn Park', 2, 1),
         ('Kilburn Park', 'Maida Vale', 2, 1), ('Maida Vale', 'Warwick Avenue', 1, 1), ('Warwick Avenue', 'Paddington', 2, 1), ('Edgware Road', 'Marylebone', 1, 1), ('Marylebone', 'Baker Street', 2, 1),
         ('Baker Street', "Regent's Park", 2, 1), ("Regent's Park", 'Oxford Circus', 2, 1), ('Oxford Circus', 'Piccadilly Circus', 2, 1), ('Piccadilly Circus', 'Charing Cross', 2, 1), ('Charing Cross', 'Embankment', 1, 1),
         ('Embankment', 'Waterloo', 2, 1), ('Waterloo', 'Lambeth North', 2, 1), ('Lambeth North', 'Elephant & Castle', 3, 1), ('Epping', 'Theydon Bois', 3, 1), ('Theydon Bois', 'Debden', 3, 1), ('Debden', 'Loughton', 2, 1),
         ('Loughton', 'Buckhurst Hill', 3, 1), ('Buckhurst Hill', 'Woodford', 2, 1), ('Woodford', 'South Woodford', 3, 1), ('South Woodford', 'Snaresbrook', 2, 1), ('Snaresbrook', 'Leytonstone', 2, 1),
         ('Roding Valley', 'Woodford', 4, 1), ('Roding Valley', 'Chigwell', 3, 1), ('Chigwell', 'Grange Hill', 2, 1), ('Grange Hill', 'Hainault', 5, 1), ('Hainault', 'Fairlop', 2, 1), ('Fairlop', 'Barkingside', 2, 1),
         ('Barkingside', 'Newbury Park', 2, 1), ('Newbury Park', 'Gants Hill', 3, 1), ('Gants Hill', 'Redbridge', 2, 1), ('Redbridge', 'Wanstead', 2, 1), ('Wanstead', 'Leytonstone', 2, 1), ('Leytonstone', 'Leyton', 2, 1),
         ('Leyton', 'Stratford', 3, 1), ('Stratford', 'Mile End', 4, 1), ('Mile End', 'Bethnal Green', 2, 1), ('Bethnal Green', 'Liverpool Street', 3, 1), ('Liverpool Street', 'Bank', 2, 1), ('Bank', "St. Paul's", 2, 1),
         ("St. Paul's", 'Chancery Lane', 2, 1), ('Chancery Lane', 'Holborn', 1, 1), ('Holborn', 'Tottenham', 2, 1), ('Tottenham', 'Oxford Circus', 1, 1), ('Oxford Circus', 'Bond Street', 2, 1), ('Bond Street', 'Marble Arch', 2, 1),
         ('Marble Arch', 'Lancaster Gate', 3, 1), ('Lancaster Gate', 'Queensway', 2, 1), ('Queensway', 'Notting Hill Gate', 2, 1), ('Notting Hill Gate', 'Holland Park', 1, 1), ('Holland Park', "Shepherd's Bush", 2, 1),
         ("Shepherd's Bush", 'White City', 3, 1), ('White City', 'East Acton', 3, 1), ('East Acton', 'North Acton', 2, 1), ('North Acton', 'Hanger Lane', 3, 1), ('North Acton', 'West Acton', 2, 1),
         ('West Acton', 'Ealing Broadway', 3, 1), ('Hanger Lane', 'Perivale', 3, 1), ('Perivale', 'Greenford', 2, 1), ('Greenford', 'Northolt', 2, 1), ('Northolt', 'South Ruislip', 3, 1), ('South Ruislip', 'Ruislip Gardens', 2, 1),
         ('Ruislip Gardens', 'West Ruislip', 3, 1), ('Paddington', 'Bayswater', 2, 1), ('Bayswater', 'Notting Hill Gate', 2, 1), ('Notting Hill Gate', 'High Street Kensington', 2, 1), ('High Street Kensington', 'Gloucester Road', 3, 1),
         ('Gloucester Road', 'South Kensington', 3, 1), ('South Kensington', 'Sloane Square', 2, 1), ('Sloane Square', 'Victoria', 2, 1), ('Victoria', "St. James's Park", 2, 1), ("St. James's Park", 'Westminster', 2, 1),
         ('Westminster', 'Embankment', 1, 1), ('Embankment', 'Temple', 2, 1), ('Temple', 'Blackfriars', 1, 1), ('Blackfriars', 'Mansion House', 2, 1), ('Mansion House', 'Cannon Street', 2, 1), ('Cannon Street', 'Monument', 1, 1),
         ('Monument', 'Tower Hill', 2, 1), ('Tower Hill', 'Aldgate', 2, 1), ('Aldgate', 'Liverpool Street', 3, 1), ('Liverpool Street', 'Moorgate', 2, 1), ('Moorgate', 'Barbican', 2, 1), ('Barbican', 'Farringdon', 1, 1),
         ('Farringdon', "King's Cross St. Pancras", 4, 1), ("King's Cross St. Pancras", 'Euston Square', 2, 1), ('Euston Square', 'Great Portland Street', 2, 1), ('Great Portland Street', 'Baker Street', 2, 1),
         ('Baker Street', 'Edgware Road', 3, 1), ('Paddington', 'Royal Oak', 2, 1), ('Royal Oak', 'Westbourne Park', 2, 1), ('Westbourne Park', 'Ladbroke Grove', 2, 1), ('Ladbroke Grove', 'Latimer Road', 2, 1),
         ('Latimer Road', 'Wood Lane', 2, 1), ('Wood Lane', "Shepherd's Bush Market", 2, 1), ("Shepherd's Bush Market", 'Goldhawk Road', 1, 1), ('Goldhawk Road', 'Hammersmith', 2, 1), ('Upminster', 'Upminster Bridge', 2, 1),
         ('Upminster Bridge', 'Hornchurch', 2, 1), ('Hornchurch', 'Elm Park', 2, 1), ('Elm Park', 'Dagenham East', 3, 1), ('Dagenham East', 'Dagenham Heathway', 2, 1), ('Dagenham Heathway', 'Becontree', 3, 1),
         ('Becontree', 'Upney', 2, 1), ('Upney', 'Barking', 3, 1), ('Barking', 'East Ham', 4, 1), ('East Ham', 'Upton Park', 2, 1), ('Upton Park', 'Plaistow', 2, 1), ('Plaistow', 'West Ham', 2, 1),
         ('West Ham', 'Bromley-by-Bow', 2, 1), ('Bromley-by-Bow', 'Bow Road', 2, 1), ('Bow Road', 'Mile End', 2, 1), ('Mile End', 'Stepney Green', 2, 1), ('Stepney Green', 'Whitechapel', 3, 1),
         ('Whitechapel', 'Aldgate East', 2, 1), ('Aldgate East', 'Tower Hill', 3, 1), ('Tower Hill', 'Monument', 2, 1), ('Monument', 'Cannon Street', 1, 1), ('Cannon Street', 'Mansion House', 2, 1),
         ('Mansion House', 'Blackfriars', 2, 1), ('Blackfriars', 'Temple', 1, 1), ('Temple', 'Embankment', 2, 1), ('Embankment', 'Westminster', 1, 1), ('Westminster', "St. James's Park", 2, 1),
         ("St. James's Park", 'Victoria', 2, 1), ('Victoria', 'Sloane Square', 2, 1), ('Sloane Square', 'South Kensington', 2, 1), ("Earl's Court", 'Kensington (Olympia)', 3, 1),
         ("Earl's Court", 'High Street Kensington', 5, 1), ('High Street Kensington', 'Notting Hill Gate', 2, 1), ('Notting Hill Gate', 'Bayswater', 2, 1), ("Earl's Court", 'West Brompton', 2, 1),
         ('West Brompton', 'Fulham Broadway', 2, 1), ('Fulham Broadway', 'Parsons Green', 2, 1), ('Parsons Green', 'Putney Bridge', 3, 1), ('Putney Bridge', 'East Putney', 3, 1), ('East Putney', 'Southfields', 2, 1),
         ('Southfields', 'Wimbledon Park', 2, 1), ('Wimbledon Park', 'Wimbledon', 4, 1), ("Earl's Court", 'West Kensington', 2, 1), ('West Kensington', 'Barons Court', 2, 1), ('Hammersmith', 'Ravenscourt Park', 2, 1),
         ('Ravenscourt Park', 'Stamford Brook', 2, 1), ('Stamford Brook', 'Turnham Green', 1, 1), ('Turnham Green', 'Gunnersbury', 3, 1), ('Gunnersbury', 'Kew Gardens', 2, 1), ('Kew Gardens', 'Richmond', 4, 1),
         ('Turnham Green', 'Chiswick Park', 2, 1), ('Chiswick Park', 'Acton Town', 2, 1), ('Ealing Common', 'Ealing Broadway', 5, 1), ('Stanmore', 'Canons Park', 4, 1), ('Canons Park', 'Queensbury', 3, 1),
         ('Queensbury', 'Kingsbury', 2, 1), ('Kingsbury', 'Wembley Park', 3, 1), ('Wembley Park', 'Neasden', 4, 1), ('Neasden', 'Dollis Hill', 2, 1), ('Dollis Hill', 'Willesden Green', 2, 1),
         ('Willesden Green', 'Kilburn', 2, 1), ('Kilburn', 'West Hampstead', 2, 1), ('West Hampstead', 'Finchley Road', 1, 1), ('Finchley Road', 'Swiss Cottage', 2, 1), ('Swiss Cottage', "St. John's Wood", 2, 1),
         ("St. John's Wood", 'Baker Street', 3, 1), ('Baker Street', 'Bond Street', 2, 1), ('Bond Street', 'Green Park', 2, 1), ('Green Park', 'Westminster', 2, 1), ('Westminster', 'Waterloo', 2, 1),
         ('Waterloo', 'Southwark', 2, 1), ('Southwark', 'London Bridge', 2, 1), ('London Bridge', 'Bermondsey', 2, 1), ('Bermondsey', 'Canada Water', 2, 1), ('Canada Water', 'Canary Wharf', 3, 1),
         ('Canary Wharf', 'North Greenwich', 3, 1), ('North Greenwich', 'Canning Town', 3, 1), ('Canning Town', 'West Ham', 3, 1), ('West Ham', 'Stratford', 2, 1), ('Amersham', 'Chalfont & Latimer', 4, 1),
         ('Chesham', 'Chalfont & Latimer', 9, 1), ('Chalfont & Latimer', 'Chorleywood', 4, 1), ('Chorleywood', 'Rickmansworth', 4, 1), ('Rickmansworth', 'Moor Park', 5, 1), ('Watford', 'Croxley', 4, 1),
         ('Croxley', 'Moor Park', 4, 1), ('Uxbridge', 'Hillingdon', 4, 1), ('Hillingdon', 'Ickenham', 2, 1), ('Ickenham', 'Ruislip', 2, 1), ('Ruislip', 'Ruislip Manor', 2, 1), ('Ruislip Manor', 'Eastcote', 2, 1),
         ('Eastcote', 'Rayners Lane', 2, 1), ('Rayners Lane', 'West Harrow', 3, 1), ('West Harrow', 'Harrow-on-the-Hill', 2, 1), ('Harrow-on-the-Hill', 'North Harrow', 3, 1), ('North Harrow', 'Pinner', 2, 1),
         ('Pinner', 'Northwood Hills', 3, 1), ('Northwood Hills', 'Northwood', 3, 1), ('Northwood', 'Moor Park', 3, 1), ('Moor Park', 'Harrow-on-the-Hill', 14, 1), ('Harrow-on-the-Hill', 'Finchley Road', 16, 1),
         ('Harrow-on-the-Hill', 'Wembley Park', 9, 1), ('Harrow-on-the-Hill', 'Northwick Park', 3, 1), ('Northwick Park', 'Preston Road', 3, 1), ('Preston Road', 'Wembley Park', 3, 1), ('Wembley Park', 'Finchley Road', 7, 1),
         ('Finchley Road', 'Baker Street', 5, 1), ('Baker Street', 'Great Portland Street', 2, 1), ('Great Portland Street', 'Euston Square', 2, 1), ('Euston Square', "King's Cross St. Pancras", 2, 1),
         ("King's Cross St. Pancras", 'Farringdon', 2, 1), ('Barbican', 'Moorgate', 2, 1), ('Moorgate', 'Liverpool Street', 2, 1), ('Liverpool Street', 'Aldgate', 3, 1), ('High Barnet', 'Totteridge & Whetstone', 4, 1),
         ('Totteridge & Whetstone', 'Woodside Park', 2, 1), ('Woodside Park', 'West Finchley', 2, 1), ('West Finchley', 'Finchley Central', 2, 1), ('Mill Hill East', 'Finchley Central', 4, 1),
         ('Finchley Central', 'East Finchley', 4, 1), ('East Finchley', 'Highgate', 3, 1), ('Highgate', 'Archway', 3, 1), ('Archway', 'Tufnell Park', 2, 1), ('Tufnell Park', 'Kentish Town', 1, 1),
         ('Kentish Town', 'Camden Town', 2, 1), ('Edgware', 'Burnt Oak', 4, 1), ('Burnt Oak', 'Colindale', 2, 1), ('Colindale', 'Hendon Central', 3, 1), ('Hendon Central', 'Brent Cross', 2, 1),
         ('Brent Cross', 'Golders Green', 3, 1), ('Golders Green', 'Hampstead', 4, 1), ('Hampstead', 'Belsize Park', 3, 1), ('Belsize Park', 'Chalk Farm', 2, 1), ('Chalk Farm', 'Camden Town', 1, 1),
         ('Camden Town', 'Mornington Crescent', 2, 1), ('Mornington Crescent', 'Euston', 2, 1), ('Warren Street', 'Euston', 1, 1), ('Warren Street', 'Goodge Street', 2, 1), ('Goodge Street', 'Tottenham Court Road', 1, 1),
         ('Tottenham Court Road', 'Leicester Square', 2, 1), ('Leicester Square', 'Charing Cross', 1, 1), ('Waterloo', 'Kennington', 3, 1), ('Euston', 'Camden Town', 4, 1), ('Euston', "King's Cross St. Pancras", 2, 1),
         ("King's Cross St. Pancras", 'Angel', 3, 1), ('Angel', 'Old Street', 3, 1), ('Old Street', 'Moorgate', 2, 1), ('Moorgate', 'Bank', 2, 1), ('Bank', 'London Bridge', 2, 1), ('London Bridge', 'Borough', 2, 1),
         ('Borough', 'Elephant & Castle', 2, 1), ('Elephant & Castle', 'Kennington', 2, 1), ('Kennington', 'Oval', 3, 1), ('Oval', 'Stockwell', 2, 1), ('Stockwell', 'Clapham North', 2, 1), ('Clapham North', 'Clapham Common', 2, 1),
         ('Clapham Common', 'Clapham South', 2, 1), ('Clapham South', 'Balham', 2, 1), ('Balham', 'Tooting Bec', 2, 1), ('Tooting Bec', 'Tooting Broadway', 2, 1), ('Tooting Broadway', 'Colliers Wood', 2, 1),
         ('Colliers Wood', 'South Wimbledon', 2, 1), ('South Wimbledon', 'Morden', 3, 1), ('Cockfosters', 'Oakwood', 2, 1), ('Oakwood', 'Southgate', 3, 1), ('Southgate', 'Arnos Grove', 4, 1), ('Arnos Grove', 'Bounds Green', 2, 1),
         ('Bounds Green', 'Wood Green', 3, 1), ('Wood Green', 'Turnpike Lane', 2, 1), ('Turnpike Lane', 'Manor House', 4, 1), ('Manor House', 'Finsbury Park Victoria', 2, 1), ('Finsbury Park Victoria', 'Arsenal', 1, 1),
         ('Arsenal', 'Holloway Road', 2, 1), ('Holloway Road', 'Caledonian Road', 2, 1), ('Caledonian Road', "King's Cross St. Pancras", 4, 1), ("King's Cross St. Pancras", 'Russell Square', 2, 1), ('Russell Square', 'Holborn Central', 2, 1),
         ('Holborn Central', 'Covent Garden', 2, 1), ('Covent Garden', 'Leicester Square', 1, 1), ('Leicester Square', 'Piccadilly Circus', 1, 1), ('Piccadilly Circus', 'Green Park', 2, 1), ('Green Park', 'Hyde Park Corner', 2, 1),
         ('Hyde Park Corner', 'Knightsbridge', 2, 1), ('Knightsbridge', 'South Kensington', 2, 1), ('South Kensington', 'Gloucester Road', 2, 1), ('Gloucester Road', "Earl's Court", 2, 1), ("Earl's Court", 'Barons Court', 3, 1),
         ('Barons Court', 'Hammersmith', 3, 1), ('Hammersmith', 'Acton Town', 8, 1), ('Hammersmith', 'Turnham Green', 4, 1), ('Turnham Green', 'Acton Town', 4, 1), ('Acton Town', 'South Ealing', 3, 1), ('South Ealing', 'Northfields', 1, 1),
         ('Northfields', 'Boston Manor', 2, 1), ('Boston Manor', 'Osterley', 3, 1), ('Osterley', 'Hounslow East', 2, 1), ('Hounslow East', 'Hounslow Central', 1, 1), ('Hounslow Central', 'Hounslow West', 3, 1),
         ('Hounslow West', 'Hatton Cross', 4, 1), ('Hatton Cross', 'Heathrow Terminals 1, 2, 3', 4, 1), ('Heathrow Terminals 1, 2, 3', 'Heathrow Terminal 5', 4, 1), ('Hatton Cross', 'Heathrow Terminal 4', 3, 1),
         ('Acton Town', 'Ealing Common', 2, 1), ('Ealing Common', 'North Ealing', 2, 1), ('North Ealing', 'Park Royal', 2, 1), ('Park Royal', 'Alperton', 2, 1), ('Alperton', 'Sudbury Town', 3, 1), ('Sudbury Town', 'Sudbury Hill', 2, 1),
         ('Sudbury Hill', 'South Harrow', 3, 1), ('South Harrow', 'Rayners Lane', 5, 1), ('Rayners Lane', 'Eastcote', 2, 1), ('Eastcote', 'Ruislip Manor', 2, 1), ('Ruislip Manor', 'Ruislip', 2, 1), ('Ruislip', 'Ickenham', 4, 1),
         ('Ickenham', 'Hillingdon', 2, 1), ('Hillingdon', 'Uxbridge', 4, 1), ('Walthamstow Central', 'Blackhorse Road', 3, 1), ('Blackhorse Road', 'Tottenham Hale', 3, 1), ('Tottenham Hale', 'Seven Sisters', 2, 1),
         ('Seven Sisters', 'Finsbury Park', 5, 1), ('Finsbury Park', 'Highbury & Islington', 2, 1), ('Highbury & Islington', "King's Cross St. Pancras", 3, 1), ("King's Cross St. Pancras", 'Euston', 2, 1),
         ('Euston', 'Warren Street', 2, 1), ('Warren Street', 'Oxford Circus', 2, 1), ('Oxford Circus', 'Green Park', 2, 1), ('Green Park', 'Victoria', 2, 1), ('Victoria', 'Pimlico', 2, 1), ('Pimlico', 'Vauxhall', 2, 1),
         ('Vauxhall', 'Stockwell', 3, 1), ('Stockwell', 'Brixton', 2, 1), ('Bank', 'Waterloo', 5, 1), ('Kenton', 'Harrow & Wealdstone', 2, 1), ('South Kenton', 'Kenton', 2, 1), ('North Wembley', 'South Kenton', 2, 1),
         ('Wembley Central', 'North Wembley', 2, 1), ('Stonebridge Park', 'Wembley Central', 2, 1), ('Harlesden', 'Stonebridge Park', 2, 1), ('Willesden Junction', 'Harlesden', 2, 1), ('Kensal Green', 'Willesden Junction', 3, 1),
         ("Queen's Park", 'Kensal Green', 2, 1), ('Kilburn Park', "Queen's Park", 2, 1), ('Maida Vale', 'Kilburn Park', 2, 1), ('Warwick Avenue', 'Maida Vale', 1, 1), ('Paddington', 'Warwick Avenue', 2, 1),
         ('Edgware Road', 'Paddington', 2, 1), ('Marylebone', 'Edgware Road', 1, 1), ('Baker Street', 'Marylebone', 2, 1), ("Regent's Park", 'Baker Street', 2, 1), ('Oxford Circus', "Regent's Park", 2, 1),
         ('Piccadilly Circus', 'Oxford Circus', 2, 1), ('Charing Cross', 'Piccadilly Circus', 2, 1), ('Lambeth North', 'Waterloo', 2, 1), ('Elephant & Castle', 'Lambeth North', 3, 1), ('Theydon Bois', 'Epping', 3, 1), ('Debden', 'Theydon Bois', 3, 1), ('Loughton', 'Debden', 2, 1), ('Buckhurst Hill', 'Loughton', 3, 1), ('Woodford', 'Buckhurst Hill', 2, 1), ('South Woodford', 'Woodford', 3, 1), ('Snaresbrook', 'South Woodford', 2, 1), ('Leytonstone', 'Snaresbrook', 2, 1), ('Woodford', 'Roding Valley', 4, 1), ('Chigwell', 'Roding Valley', 3, 1), ('Grange Hill', 'Chigwell', 2, 1), ('Hainault', 'Grange Hill', 5, 1), ('Fairlop', 'Hainault', 2, 1), ('Barkingside', 'Fairlop', 2, 1), ('Newbury Park', 'Barkingside', 2, 1), ('Gants Hill', 'Newbury Park', 3, 1), ('Redbridge', 'Gants Hill', 2, 1), ('Wanstead', 'Redbridge', 2, 1), ('Leytonstone', 'Wanstead', 2, 1), ('Leyton', 'Leytonstone', 2, 1), ('Stratford', 'Leyton', 3, 1), ('Mile End', 'Stratford', 4, 1), ('Bethnal Green', 'Mile End', 2, 1), ('Liverpool Street', 'Bethnal Green', 3, 1), ('Bank', 'Liverpool Street', 2, 1), ("St. Paul's", 'Bank', 2, 1), ('Chancery Lane', "St. Paul's", 2, 1), ('Holborn', 'Chancery Lane', 1, 1), ('Tottenham', 'Holborn', 2, 1), ('Oxford Circus', 'Tottenham', 1, 1), ('Bond Street', 'Oxford Circus', 2, 1), ('Marble Arch', 'Bond Street', 2, 1), ('Lancaster Gate', 'Marble Arch', 3, 1), ('Queensway', 'Lancaster Gate', 2, 1), ('Notting Hill Gate', 'Queensway', 2, 1), ('Holland Park', 'Notting Hill Gate', 1, 1), ("Shepherd's Bush", 'Holland Park', 2, 1), ('White City', "Shepherd's Bush", 3, 1), ('East Acton', 'White City', 3, 1), ('North Acton', 'East Acton', 2, 1), ('Hanger Lane', 'North Acton', 3, 1), ('West Acton', 'North Acton', 2, 1), ('Ealing Broadway', 'West Acton', 3, 1), ('Perivale', 'Hanger Lane', 3, 1), ('Greenford', 'Perivale', 2, 1), ('Northolt', 'Greenford', 2, 1), ('South Ruislip', 'Northolt', 3, 1), ('Ruislip Gardens', 'South Ruislip', 2, 1), ('West Ruislip', 'Ruislip Gardens', 2, 1), ('Paddington', 'Edgware Road', 3, 1), ('Bayswater', 'Paddington', 2, 1), ('Gloucester Road', 'High Street Kensington', 3, 1), ('Aldgate', 'Tower Hill', 2, 1), ('Farringdon', 'Barbican', 1, 1), ('Edgware Road', 'Baker Street', 3, 1), ('Royal Oak', 'Paddington', 2, 1), ('Westbourne Park', 'Royal Oak', 2, 1), ('Ladbroke Grove', 'Westbourne Park', 2, 1), ('Latimer Road', 'Ladbroke Grove', 2, 1), ('Wood Lane', 'Latimer Road', 2, 1), ("Shepherd's Bush Market", 'Wood Lane', 2, 1), ('Goldhawk Road', "Shepherd's Bush Market", 1, 1), ('Hammersmith', 'Goldhawk Road', 2, 1), ('Upminster Bridge', 'Upminster', 2, 1), ('Hornchurch', 'Upminster Bridge', 2, 1), ('Elm Park', 'Hornchurch', 2, 1), ('Dagenham East', 'Elm Park', 3, 1), ('Dagenham Heathway', 'Dagenham East', 2, 1), ('Becontree', 'Dagenham Heathway', 3, 1), ('Upney', 'Becontree', 2, 1), ('Barking', 'Upney', 3, 1), ('East Ham', 'Barking', 4, 1), ('Upton Park', 'East Ham', 2, 1), ('Plaistow', 'Upton Park', 2, 1), ('West Ham', 'Plaistow', 2, 1), ('Bromley-by-Bow', 'West Ham', 2, 1), ('Bow Road', 'Bromley-by-Bow', 2, 1), ('Mile End', 'Bow Road', 2, 1), ('Stepney Green', 'Mile End', 2, 1), ('Whitechapel', 'Stepney Green', 3, 1), ('Aldgate East', 'Whitechapel', 2, 1), ('Tower Hill', 'Aldgate East', 3, 1), ("Earl's Court", 'Gloucester Road', 2, 1), ('Kensington (Olympia)', "Earl's Court", 3, 1), ('High Street Kensington', "Earl's Court", 5, 1), ('West Brompton', "Earl's Court", 2, 1), ('Fulham Broadway', 'West Brompton', 2, 1), ('Parsons Green', 'Fulham Broadway', 2, 1), ('Putney Bridge', 'Parsons Green', 3, 1), ('East Putney', 'Putney Bridge', 3, 1), ('Southfields', 'East Putney', 2, 1), ('Wimbledon Park', 'Southfields', 2, 1), ('Wimbledon', 'Wimbledon Park', 4, 1), ('West Kensington', "Earl's Court", 2, 1), ('Barons Court', 'West Kensington', 2, 1), ('Hammersmith', 'Barons Court', 3, 1), ('Ravenscourt Park', 'Hammersmith', 2, 1), ('Stamford Brook', 'Ravenscourt Park', 2, 1), ('Turnham Green', 'Stamford Brook', 1, 1), ('Gunnersbury', 'Turnham Green', 3, 1), ('Kew Gardens', 'Gunnersbury', 2, 1), ('Richmond', 'Kew Gardens', 4, 1), ('Chiswick Park', 'Turnham Green', 2, 1), ('Acton Town', 'Chiswick Park', 2, 1), ('Ealing Common', 'Acton Town', 2, 1), ('Ealing Broadway', 'Ealing Common', 5, 1), ('Liverpool Street', 'Aldgate East', 3, 1), ('Canons Park', 'Stanmore', 4, 1), ('Queensbury', 'Canons Park', 3, 1), ('Kingsbury', 'Queensbury', 2, 1), ('Wembley Park', 'Kingsbury', 3, 1), ('Neasden', 'Wembley Park', 4, 1), ('Dollis Hill', 'Neasden', 2, 1), ('Willesden Green', 'Dollis Hill', 2, 1), ('Kilburn', 'Willesden Green', 2, 1), ('West Hampstead', 'Kilburn', 2, 1), ('Finchley Road', 'West Hampstead', 1, 1), ('Swiss Cottage', 'Finchley Road', 2, 1), ("St. John's Wood", 'Swiss Cottage', 2, 1), ('Baker Street', "St. John's Wood", 3, 1), ('Bond Street', 'Baker Street', 2, 1), ('Green Park', 'Bond Street', 2, 1), ('Westminster', 'Green Park', 2, 1), ('Waterloo', 'Westminster', 2, 1), ('Southwark', 'Waterloo', 2, 1), ('London Bridge', 'Southwark', 2, 1), ('Bermondsey', 'London Bridge', 2, 1), ('Canada Water', 'Bermondsey', 2, 1), ('Canary Wharf', 'Canada Water', 3, 1), ('North Greenwich', 'Canary Wharf', 3, 1), ('Canning Town', 'North Greenwich', 3, 1), ('Stratford', 'West Ham', 2, 1), ('Chalfont & Latimer', 'Amersham', 4, 1), ('Chalfont & Latimer', 'Chesham', 9, 1), ('Chorleywood', 'Chalfont & Latimer', 4, 1), ('Rickmansworth', 'Chorleywood', 4, 1), ('Moor Park', 'Rickmansworth', 5, 1), ('Croxley', 'Watford', 4, 1), ('Moor Park', 'Croxley', 4, 1), ('West Harrow', 'Rayners Lane', 3, 1), ('Harrow-on-the-Hill', 'West Harrow', 2, 1), ('North Harrow', 'Harrow-on-the-Hill', 3, 1), ('Pinner', 'North Harrow', 2, 1), ('Northwood Hills', 'Pinner', 3, 1), ('Northwood', 'Northwood Hills', 3, 1), ('Moor Park', 'Northwood', 3, 1), ('Harrow-on-the-Hill', 'Moor Park', 14, 1), ('Finchley Road', 'Harrow-on-the-Hill', 16, 1), ('Wembley Park', 'Harrow-on-the-Hill', 9, 1), ('Northwick Park', 'Harrow-on-the-Hill', 3, 1), ('Preston Road', 'Northwick Park', 3, 1), ('Wembley Park', 'Preston Road', 3, 1), ('Finchley Road', 'Wembley Park', 7, 1), ('Baker Street', 'Finchley Road', 5, 1), ('Totteridge & Whetstone', 'High Barnet', 4, 1), ('Woodside Park', 'Totteridge & Whetstone', 2, 1), ('West Finchley', 'Woodside Park', 2, 1), ('Finchley Central', 'West Finchley', 2, 1), ('Finchley Central', 'Mill Hill East', 4, 1), ('East Finchley', 'Finchley Central', 4, 1), ('Highgate', 'East Finchley', 3, 1), ('Archway', 'Highgate', 3, 1), ('Tufnell Park', 'Archway', 2, 1), ('Kentish Town', 'Tufnell Park', 1, 1), ('Camden Town', 'Kentish Town', 2, 1), ('Burnt Oak', 'Edgware', 4, 1), ('Colindale', 'Burnt Oak', 2, 1), ('Hendon Central', 'Colindale', 3, 1), ('Brent Cross', 'Hendon Central', 2, 1), ('Golders Green', 'Brent Cross', 3, 1), ('Hampstead', 'Golders Green', 4, 1), ('Belsize Park', 'Hampstead', 3, 1), ('Chalk Farm', 'Belsize Park', 2, 1), ('Camden Town', 'Chalk Farm', 1, 1), ('Mornington Crescent', 'Camden Town', 2, 1), ('Euston', 'Mornington Crescent', 2, 1), ('Goodge Street', 'Warren Street', 2, 1), ('Tottenham Court Road', 'Goodge Street', 1, 1), ('Leicester Square', 'Tottenham Court Road', 2, 1), ('Charing Cross', 'Leicester Square', 1, 1), ('Embankment', 'Charing Cross', 1, 1), ('Waterloo', 'Embankment', 2, 1), ('Kennington', 'Waterloo', 3, 1), ('Camden Town', 'Euston', 4, 1), ('Angel', "King's Cross St. Pancras", 3, 1), ('Old Street', 'Angel', 3, 1), ('Moorgate', 'Old Street', 2, 1), ('Bank', 'Moorgate', 2, 1), ('London Bridge', 'Bank', 2, 1), ('Borough', 'London Bridge', 2, 1), ('Elephant & Castle', 'Borough', 2, 1), ('Kennington', 'Elephant & Castle', 2, 1), ('Oval', 'Kennington', 3, 1), ('Stockwell', 'Oval', 2, 1), ('Clapham North', 'Stockwell', 2, 1), ('Clapham Common', 'Clapham North', 2, 1), ('Clapham South', 'Clapham Common', 2, 1), ('Balham', 'Clapham South', 2, 1), ('Tooting Bec', 'Balham', 2, 1), ('Tooting Broadway', 'Tooting Bec', 2, 1), ('Colliers Wood', 'Tooting Broadway', 2, 1), ('South Wimbledon', 'Colliers Wood', 2, 1), ('Morden', 'South Wimbledon', 3, 1), ('Oakwood', 'Cockfosters', 2, 1), ('Southgate', 'Oakwood', 3, 1), ('Arnos Grove', 'Southgate', 4, 1), ('Bounds Green', 'Arnos Grove', 2, 1), ('Wood Green', 'Bounds Green', 3, 1), ('Turnpike Lane', 'Wood Green', 2, 1), ('Manor House', 'Turnpike Lane', 4, 1), ('Finsbury Park Victoria', 'Manor House', 2, 1), ('Arsenal', 'Finsbury Park Victoria', 1, 1), ('Holloway Road', 'Arsenal', 2, 1), ('Caledonian Road', 'Holloway Road', 2, 1), ("King's Cross St. Pancras", 'Caledonian Road', 4, 1), ('Russell Square', "King's Cross St. Pancras", 2, 1), ('Holborn Central', 'Russell Square', 2, 1), ('Covent Garden', 'Holborn Central', 2, 1), ('Leicester Square', 'Covent Garden', 1, 1), ('Piccadilly Circus', 'Leicester Square', 1, 1), ('Green Park', 'Piccadilly Circus', 2, 1), ('Hyde Park Corner', 'Green Park', 2, 1), ('Knightsbridge', 'Hyde Park Corner', 2, 1), ('South Kensington', 'Knightsbridge', 2, 1), ('Barons Court', "Earl's Court", 3, 1), ('Acton Town', 'Hammersmith', 8, 1), ('Turnham Green', 'Hammersmith', 4, 1), ('Acton Town', 'Turnham Green', 4, 1), ('South Ealing', 'Acton Town', 3, 1), ('Northfields', 'South Ealing', 1, 1), ('Boston Manor', 'Northfields', 2, 1), ('Osterley', 'Boston Manor', 3, 1), ('Hounslow East', 'Osterley', 2, 1), ('Hounslow Central', 'Hounslow East', 1, 1), ('Hounslow West', 'Hounslow Central', 3, 1), ('Hatton Cross', 'Hounslow West', 4, 1), ('Heathrow Terminals 1, 2, 3', 'Hatton Cross', 4, 1), ('Heathrow Terminal 5', 'Heathrow Terminals 1, 2, 3', 4, 1), ('Heathrow Terminal 4', 'Hatton Cross', 3, 1), ('North Ealing', 'Ealing Common', 2, 1), ('Park Royal', 'North Ealing', 2, 1), ('Alperton', 'Park Royal', 2, 1), ('Sudbury Town', 'Alperton', 3, 1), ('Sudbury Hill', 'Sudbury Town', 2, 1), ('South Harrow', 'Sudbury Hill', 3, 1), ('Rayners Lane', 'South Harrow', 5, 1), ('Blackhorse Road', 'Walthamstow Central', 3, 1), ('Tottenham Hale', 'Blackhorse Road', 3, 1), ('Seven Sisters', 'Tottenham Hale', 2, 1), ('Finsbury Park', 'Seven Sisters', 5, 1), ('Highbury & Islington', 'Finsbury Park', 2, 1), ("King's Cross St. Pancras", 'Highbury & Islington', 3, 1), ('Oxford Circus', 'Warren Street', 2, 1), ('Green Park', 'Oxford Circus', 2, 1), ('Victoria', 'Green Park', 2, 1), ('Pimlico', 'Victoria', 2, 1), ('Vauxhall', 'Pimlico', 2, 1), ('Stockwell', 'Vauxhall', 3, 1), ('Brixton', 'Stockwell', 2, 1), ('Waterloo', 'Bank', 5, 1)]


#edges is also used when making the graph and works by adding ditence valuess between the vertices definded above 

def getEdgeTimes(start, end):
    for edge in edges:
        if (vertices[start] == edge[0] and vertices[end] == edge[1]) or (vertices[start] == edge[1] and vertices[end] == edge[0]):
            return edge[2]
#a callable function that gets the distence between two vertices using the edge values, made callable so it
#can be used multiple times within the same run of the program and return differnt values
        
def journeyPlanner():
        global timesList
        global d
        value = 0
        trainGraph = AdjacencyListGraph(len(vertices), True, True)
#this defines our stations graph using the pre provided AdjacencyListGraph code/modual to assign the nessary
#aguments to allow for the edges between vertices

        for edge in edges:
                trainGraph.insert_edge(vertices.index(edge[0]), vertices.index(edge[1]), edge[3])
#a for loop that for every value in edges (distences between two vertices) it will insert the edge tuple with all
#its values into the defined train graph
        
        d, pi = dijkstra(trainGraph, vertices.index(finish))

#definging two values by using the pre provided dijkstra taking two agunmentsn the graph with all station data
#and the value finish which is the input varible from the stat representing the usser desired desstination

        stationLists = [[] for _ in range(len(vertices))]
        timesList = [[] for _ in range(len(vertices))]
#defining a list that storess all the connecting verticies to the oringal giving verticy and one just for the times

        for i in range(len(pi)):
            if pi[i] is not None:
                currentStation = i
                value = 0
                while pi[currentStation] is not None:
                    lastStation = pi[currentStation]
                    value = value + 1
                    timesList[i].append(str(getEdgeTimes(lastStation, currentStation)))
                    stationLists[i].append(str(value) + " Stop(" + str(getEdgeTimes(lastStation, currentStation)) + " mins)"" -> " + vertices[lastStation])
                    currentStation = lastStation
#this for loop is used for the output of the travaling stations between stops using a counter to run throught all
#the stations the journy takess to saves them line by line with the ssstation name and time to a lisst aswell as
#the addition of the amount of stops


        x = vertices.index(start)
        print(vertices[x] + ": total stops of ("+ str(d[x]) + "), stations = ['"+vertices[x]+"'] "+ str(stationLists[x]))
#final overall output priting the starting station, the total time of the journy and the sstations list from before

        

while True:
        histogramData = []
        start = input("Starting Station: ")
        finish = input("End Station: " )
        journeyPlanner()
        for i in range(len(vertices)):
            histogramData.append(d[i])
        histogramData = [x for x in histogramData if x != float("inf")]
        plt.xlabel('Stops')
        plt.ylabel('Frequency')
        plt.title('Travel Times')
        plt.hist(histogramData, edgecolor='black')
        plt.show() 
#the starting input values that ask the user for thier starting station and thier desired destinaion, this
#value is used later in the actual logicn of the program
#the starting input values that ask the user for thier starting station and thier desired destinaion, this
#value is used later in the actual logicn of the program plus a function to get the histogram data


