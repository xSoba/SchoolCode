import numpy as np
#To be more efficient our array now stores all information the needs to be retrieved
races = np.array(
            [   #Human syllables
                [
                        #Male syllables
                    [
                        #Beginning Syllables
                        ["Tho","Geo","Ru","Da","Ni","Ro","Mi","Wi","Kri",'Tri'],
                        #Middle Syllables
                        ["thu", "car","ma","ha","car","sti","per","jam","li","am"],
                        #End Syllables
                        ["n","op","ert","er","an","ew","ack","en","an","in"],
                    ],
                    [
                        #Female syllables

                        #Beginning Syllables
                        ['Ab','Li','Ame','Je','Ev','Ol','El','A','E','So'],
                        #Middle Syllables
                        ['be','me','ve','an','mm','un','ar','za','bi','ga'],
                        #End Syllables
                        ['er','ly','ta','th','ma','ia','a','la','yn','or'],
                    ],
                ],
                #Orc syllables
                [
                    #Male orc syllables   
                    [
                        #Beginning Syllables
                        ['','','','','','','','','',''],
                        #Middle Syllables
                        ['','','','','','','','','',''],
                        #End Syllables
                        ['','','','','','','','','',''],
                    ],
                    #Female orc syllables
                    [
                        #Beginning Syllables
                        ['','','','','','','','','',''],
                        #Middle Syllables
                        ['','','','','','','','','',''],
                        #End Syllables
                        ['','','','','','','','','',''],
                    ],
                ],
                #Elf syllables
                [
                    #Male elf syllables
                    [
                        #Beginning Syllables
                        ['','','','','','','','','',''],
                        #Middle Syllables
                        ['','','','','','','','','',''],
                        #End Syllables
                        ['','','','','','','','','',''],
                    ],
                    #Female elf syllables
                    [
                        #Beginning Syllables
                        ['','','','','','','','','',''],
                        #Middle Syllables
                        ['','','','','','','','','',''],
                        #End Syllables
                        ['','','','','','','','','',''],
                    ],

                ],
            ], 
            
            
            
            
dtype=str)


#Our Array is now listed as Follows. races[<race>][<Gender>][<SyllablePosition>]
name = np.empty([1,1] , dtype=str)
#[]
#This option array is made of three rows and three columns
opt = np.empty([0,3], dtype=int)
#Representation of this is 
#[[]
# []
# []]

pos = 0
