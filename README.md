# Random Presenter

This repository is a fun way to pick out a person (i.e. from a lab team or office) at random for a particular task. It can be useful for presentations (which was the original intention), but also for various other activities where a random person needs to be chosen. 

Photos for illustration purposes were taken from the [FACES database](https://faces.mpdl.mpg.de/imeji/collection/IXTdg721TwZwyZ8e?q=).

It is recommended that you replace these photos with the photos of your colleagues and name them "FirstName_LastName.jpg".
You can also replace the company logo with the one of your institution (and name it "logo.png") as well as the company name (line 88), which is displayed in the center of the GUI.

__Python Version: 3.7__

## Clone repository

```
$ git clone https://github.com/tadorfer/random-presenter.git
```

## Install required package

Apart from PIL, all packages are part of the Python Standard Library. Thus, we need to first run:

```
$ conda install -c anaconda pil
```

## Execute 

In order to execute the script, run:

```
python3 random_presenter.py
```

After executing the above code cell, the GUI will open and the photos of the group will start circling around the company name. 

<p align="center">
  <img src="/Output/Members.png" height="700" width="650">
 </p>

After pressing start, the countdown starts from 5 and will then reveal the randomly chosen person for the desired task.

<p align="center">
  <img src="/Output/Presenter.png" height="700" width="650">
</p>

