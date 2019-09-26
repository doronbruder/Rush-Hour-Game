class Car:
    """
    This class represent a car that can  be used for the game "rush hour"
    """
    HORIZONTAL=1
    VERTICAL=0

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.__name=name
        self.__length=length
        self.__location=location
        self.__orientation=orientation



    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        length=self.__length
        location=self.__location
        orientation=self.__orientation
        coordinates_lst=[location]
        # Check the cases where the car is horizontal and vertical
        if orientation==Car.HORIZONTAL:
            for col in range(1,length):
                coordinates_lst.append((location[0],location[1]+col))
        if orientation==Car.VERTICAL:
            for row in range(1,length):
                coordinates_lst.append((location[0]+row,location[1]))
        return coordinates_lst


    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        orientation=self.__orientation
        possible_moves_dic={}
        if orientation==Car.HORIZONTAL:
            possible_moves_dic={'l': "Car can moves left", 'r':"Car can moves right"}
        elif(orientation==Car.VERTICAL):
            possible_moves_dic= {'u':"Car can moves up",'d':"Car can moves down"}
        return possible_moves_dic


    def movement_requirements(self, movekey):
        """
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        car_coor=self.car_coordinates()
        must_be_empty = []
        # Go over all the options according different directions
        if self.__orientation==1:
            if movekey == 'l':
                left_coor=car_coor[0]
                must_be_empty.append((left_coor[0], left_coor[1] -( 1)))
            elif movekey == 'r':
                right_coor=car_coor[-1]
                must_be_empty.append((right_coor[0], right_coor[1]+1))

        elif self.__orientation==0:
            if movekey == 'u':
                upper_coor=car_coor[0]
                must_be_empty.append((upper_coor[0] - 1, upper_coor[1]))
            elif movekey == 'd':
                bottom_coor=car_coor[-1]
                must_be_empty.append((bottom_coor[0]+1 ,bottom_coor[1]))

        return must_be_empty



    def move(self, movekey):
        """
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        # Go over all the options according the different directions
        if self.__orientation==1 and movekey=='l':
            new_location= self.__location[0], self.__location[1] - 1
            self.__location=new_location
            return True
        elif self.__orientation==1 and movekey=='r':
            new_location= self.__location[0], self.__location[1] + 1
            self.__location=new_location
            return True
        elif self.__orientation==0 and movekey=='u':
            new_location= self.__location[0] - 1, self.__location[1]
            self.__location = new_location

            return True
        elif self.__orientation==0 and movekey=='d':
            new_location= self.__location[0] + 1, self.__location[1]
            self.__location = new_location

            return True
        else:
            return False





    def get_name(self):
        """
        :return: The name of this car.
        """
        car_name=self.__name
        return car_name


