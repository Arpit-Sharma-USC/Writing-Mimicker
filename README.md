# Writing-Mimicker
An LSTM to mimic the writing style of prominent British Mathematician, Philosopher, prolific writer, and political activist, Bertrand Russell.

# Procedure

•	I used the append method to add the content of a text file onto a file stream and then saved it in a text file. 
•	I then used extended ASCII N=256 characters to represent characters 
•	A window size of 100 was selected to teach the LSTM 
•	I used OneHotEncoding in sklearn to perform this task.
•	Understanding the requirements of the softmax output layer:
    o	Cross entropy indicates the distance between what the model believes the output distribution should be, and what the original             distribution really is. It is defined as,         
      
        H ( y , p )=−∑ ylog ( p ) 
        
    o	Cross entropy measure is a widely used alternative of squared error. 
•	I trained the model for 20 epochs and then for 50 epochs and observed the differences.
•	I have combined the result of this part with the next. Please go through the ‘Results’ for further insight on this. 
•	I then stored each set of weights in an hdf5 file and the one with least loss was picked.



# Noteworthy Observations:
Clearly the model struggles to even predict words let alone the grammar whe nthe loss is high as in the case of running 20 epochs. It picked up certain words like ‘just’ and observed ‘as’ followed it. So in almost every predcition it followed “just” with an “as’.
After running higher number of epochs the model was able to predict the words flawlessly but the pattern of “just-as ” followed suite here as well. It was unable to properly predcit the grammar and make meaningful sentences but the words were spelled correctly.
