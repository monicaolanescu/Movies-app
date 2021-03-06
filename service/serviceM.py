'''
Created on Nov 13, 2017

@author: Monica
'''
from domain.movie import movie
import random
from sort.sorting import sorting
from sort.algorithms.Algorithm import Algorithm

class moviesService:
    def __init__(self,repo,valid):
        '''
        initializes the class
        in:    -> repo:repoMovies
               -> valid:validatorMovie
        '''
        self.__repository=repo
        self.__validator=valid
        
    def createMovie(self,idM,title,genre,description):
        '''
        creates a movie
        in:   ->idM:int unique
              ->title:string
              ->genre:string
              ->description:string
        out:the movie created
        '''
        m=movie(idM,title,genre,description)
        self.__validator.validate(m)
        self.__repository.store(m)
        return m
    
    def update(self,idM,title,genre,descr):
        '''
        updates a movie 
        '''
        m=movie(idM,title,genre,descr)
        self.__validator.validate(m)
        self.__repository.modify(m)
       
    
    def remove(self,idM):
        '''
        removes a movie with an unique id:idM(in ->integer number)
        '''
        self.__repository.remove(idM)
    
    def removeAll(self):
        '''
        removes all movies
        '''
        self.__repository.clearList()
        
    def find(self,nameK,valueK):
        '''
        find movies with a specified key
        in:  ->nameK(the name of key):can be id/title/genre
             ->valueK(the value of key)
        out: the movie
        '''
        #return self.__repository.find(nameK,valueK)
        lst=self.__repository.getAll()
        found=[]
        return self.__repository.findRec(nameK,valueK,lst,found)
    
    def filterBy(self,nameK,valueK):
        '''
        find movies with a specified key whose value is a string
        in:  ->nameK(the name of key):can be title/genre in this case
             ->valueK(the value of key)
        out: the movie
        '''
        allMovies=self.__repository.getAll()
        filteredMovies=[]
        for i in range(len(allMovies)):
            if (nameK=="title" and allMovies[i].getTitle()==valueK) or\
                (nameK=="genre" and allMovies[i].getGenre()==valueK) :
                filteredMovies.append(allMovies[i])
        return filteredMovies
       
    def filterByRec(self,nameK,valueK,lst,found):
        '''
        find movies with a specified key whose value is a string
        in:  ->nameK(the name of key):can be title/genre in this case
             ->valueK(the value of key)
        out: the movie
        '''
        if lst==[] and len(found)!=0:
            return found
        elif lst==[]:
            raise ("It doesn't exist!\n")
        elif (nameK=="title" and lst[0].getTitle()==valueK) or\
                (nameK=="genre" and lst[0].getGenre()==valueK) :
                found.append(lst[0])
                return self.findRec(nameK,valueK,lst[1:],found)
        else:
            return self.findRec(nameK,valueK,lst[1:],found)
     
  
    
    def sortBy(self,nameK):
        '''
        sorts the list of movies by a specified key,whose value is an integer number
        in:nameK (the key)
        out:-
        '''
        if nameK=="id":
            #return sorted(self.__repository.getAll(), key=lambda k:k.getId(),reverse=True)
            #return bingoSort(self.getAll(), key=lambda k:k.getId(), reverse=True).sort(self.getAll())
            return sorting.sort(self.getAll(), key=lambda k:k.getId(), reverse=True, algorithm=Algorithm.MERGE_SORT)
            
    def get(self,idM):
        '''
        gets a movie
        in:the unique id (idM) -an integer number
        out:the movie
        '''
        return self.__repository.get(idM)
    
    def getAll(self):
        '''
        gets all the movies
        in:-
        out:the list of movies
        '''
        return self.__repository.getAll()
    
    def getNrMovies(self):
        '''
        gets the number of movies
        in:-
        out:the number of movies
        '''
        return self.__repository.sizeOfList()
    
    def getAllId(self):
        '''
        get a list with integer element with all the movies id
        '''
        lst=[]
        for i in self.getAll():
            lst.append(int(i.getId()))
            
        return lst
    
    def populateRandom(self,limit):
        while limit!=0:
            idM=random.randrange(1000)
            title=random.choices(["Me before you","Inception","Divergent","If I stay","It","The age of Adaline","The everlasting","Interstellar"])[0]
            genre=random.choices(["Love","Drama","Horror","Comedy","Action","SF"])[0]
            description=random.choices(["The best","Amazing","The worst","Good","Wonderful",])[0]
            #self.createMovie(idM,title,genre,description)
            self.__repository.store(movie(idM,title,genre,description))
            limit-=1
        return limit
