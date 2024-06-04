def tx(text: str) -> str:
    """Performs minor formatting on text."""
    cleaned_text = text.replace("\n", " ").replace("\t", " ")
    # Other potential text formatting functions can go here
    print(cleaned_text)


a = """The evidence against him will include testimony about how the gun at the center the case ended up in a trash can outside Janssen's Market, an upscale grocer in Delaware's monied Greenville area. 
       The proceeding will include testimony by a former Delaware State Police official who investigated that incident, as well as the person who trashed the gun: Biden's then-lover and widow of his late brother."""


tx(a)
