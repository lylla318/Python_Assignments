# breakout.py
# LYLLA YOUNES, LEY23
# DATE COMPLETED HERE
"""Primary module for Breakout application

This module contains the App controller class for the Breakout application.
There should not be any need for additional classes in this module.
If you need more classes, 99% of the time they belong in either the gameplay
module or the models module. If you are ensure about where a new class should go, 
post a question on Piazza."""
from constants import *
# breakout.py
# LYLLA YOUNES, LEY23
# DATE COMPLETED HERE
"""Primary module for Breakout application

This module contains the App controller class for the Breakout application.
There should not be any need for additional classes in this module.
If you need more classes, 99% of the time they belong in either the gameplay
module or the models module. If you are ensure about where a new class should go, 
post a question on Piazza."""
from constants import *
from models import *
from gameplay import *
from game2d import *
import time


# PRIMARY RULE: Breakout can only access attributes in gameplay.py via getters/setters
# Breakout is NOT allowed to access anything in models.py

class Breakout(GameApp):
    """Instance is a Breakout App
    
    This class extends GameApp and implements the various methods necessary 
    for processing the player inputs and starting/running a game.
    
        Method init starts up the game.
        
        Method update either changes the state or updates the Gameplay object
        
        Method draw displays the Gameplay object and any other elements on screen
    
    Because of some of the weird ways that Kivy works, you SHOULD NOT create an
    initializer __init__ for this class.  Any initialization should be done in
    the init method instead.  This is only for this class.  All other classes
    behave normally.
    
    Most of the work handling the game is actually provided in the class Gameplay.
    Gameplay should have a minimum of two methods: updatePaddle(touch) which moves
    the paddle, and updateBall() which moves the ball and processes all of the
    game physics. This class should simply call that method in update().
    
    The primary purpose of this class is managing the game state: when is the 
    game started, paused, completed, etc. It keeps track of that in an attribute
    called _state.
    
    INSTANCE ATTRIBUTES:
        view    [Immutable instance of GView, it is inherited from GameApp]:
            the game view, used in drawing (see examples from class)
        _state  [one of STATE_INACTIVE, STATE_COUNTDOWN, STATE_PAUSED, STATE_ACTIVE]:
            the current state of the game represented a value from constants.py
        _last   [GPoint, or None if mouse button is not pressed]:
            the last mouse position (if Button was pressed)
        _game   [GModel, or None if there is no game currently active]: 
            the game controller, which manages the paddle, ball, and bricks
        
    
    ADDITIONAL INVARIANTS: Attribute _game is only None if _state is STATE_INACTIVE.
    
    You may have more attributes if you wish (you might need an attribute to store
    any text messages you display on the screen). If you add new attributes, they
    need to be documented here.
        
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    
    _welcome_message [GLabel, or None if there is no game currently active]:
            the welcome message, which is a few words of text
    _pause_message1 [GLabel, or None if there is no game currently active]:
            the two lives left message, which is a few words of text
    _pause_message2 [GLabel, or None if there is no game currently active]:
            the one lives left message, which is a few words of text
    _gameOver_message [GLabel, or None if there is no game currently active]:
            the game over message, which is a few words of text
    _youWin_message [GLabel, or None if there is no game currently active]:
            message for when player wins, which is a few words of text
    _get_new_message [GLabel, or None if there is no game currently active]:
            message telling player to click for new serve, which is a few words of text
    _youWin_message [GLabel, or None if there is no game currently active]:
            message telling player to click for new game, which is a few words of text
    _time [int >= 0, 0 if mouse state changed]: #wording taken from touch.py
            by Walker White
            frames since mouse last changed (pressed, released)
    _lives [int >= 0 and <=3]
            determines number of lives left in game
    
    
    Attribute _message:
    If the state is STATE_INACTIVE, then there is a welcome message
    If the state is not STATE_INACTIVE, the welcome message is None.

    """
    
    # DO NOT MAKE A NEW INITIALIZER!
    
    # GAMEAPP METHODS
    def init(self):
        """Initialize the game state.
        
        This method is distinct from the built-in initializer __init__.
        This method is called once the game is running. You should use
        it to initialize any game specific attributes.
        
        This method should initialize any state attributes as necessary 
        to statisfy invariants. When done, set the _state to STATE_INACTIVE
        and create a message (in attribute _mssg) saying that the user should 
        press to play a game."""
        
        self._state = STATE_INACTIVE
        self._last = None
        self._game = None
        self._time = 0
        self._lives = 3
        self._welcome_message = GLabel(x=80,y=250,text='Press to Play',font_size=50,
                               halign='left',valign='bottom',
                               linecolor=colormodel.RGB(0,76,153), bold=True)
        self._pause_message1 = GLabel(x=120,y=250,text='Two lives left',font_size=40,
                               halign='left',valign='bottom',
                               linecolor=colormodel.RGB(0,76,153), bold=True)
        self._pause_message2 = GLabel(x=120,y=250,text='One life left',font_size=40,
                               halign='left',valign='bottom',
                               linecolor=colormodel.RGB(0,76,153), bold=True)
        self._get_new_message = GLabel(x=88,y=200,text='Click for new ball.',font_size=40,
                               halign='left',valign='bottom',
                               linecolor=colormodel.RGB(0,76,153), bold=True)
        self._gameOver_message = GLabel(x=100,y=250,text='Game Over',font_size=50,
                               halign='left',valign='bottom',
                               linecolor=colormodel.RGB(0,76,153), bold=True)
        self._youWin_message = GLabel(x=115,y=250,text='You Win!',font_size=50,
                               halign='left',valign='bottom',
                               linecolor=colormodel.RGB(0,76,153), bold=True)
        self._newGame_message = GLabel(x=70,y=200,text='Click to start new game.',font_size=30,
                               halign='left',valign='bottom',
                               linecolor=colormodel.RGB(0,76,153), bold=True)
            
    
    def update(self,dt):
        """Animate a single frame in the game.
        
        It is the method that does most of the work. Of course, it should
        rely on helper methods in order to keep the method short and easy
        to read.  Some of the helper methods belong in this class, but most
        of the others belong in class Gameplay.
        
        The first thing this method should do is to check the state of the
        game. We recommend that you have a helper method for every single
        state: STATE_INACTIVE, STATE_COUNTDOWN, STATE_PAUSED, STATE_ACTIVE.
        The game does different things in each state.
        
        In STATE_INACTIVE, the method checks to see if the player clicks
        the mouse (_last is None, but view.touch is not None). If so, it 
        (re)starts the game and switches to STATE_COUNTDOWN.
        
        STATE_PAUSED is similar to STATE_INACTIVE. However, instead of 
        restarting the game, it simply switches to STATE_COUNTDOWN.
        
        In STATE_COUNTDOWN, the game counts down until the ball is served.
        The player is allowed to move the paddle, but there is no ball.
        Paddle movement should be handled by class Gameplay (NOT in this class).
        This state should delay at least one second.
        
        In STATE_ACTIVE, the game plays normally.  The player can move the
        paddle and the ball moves on its own about the board.  Both of these
        should be handled by methods inside of class Gameplay (NOT in this class).
        Gameplay should have methods named updatePaddle and updateBall.
        
        While in STATE_ACTIVE, if the ball goes off the screen and there
        are tries left, it switches to STATE_PAUSED.  If the ball is lost 
        with no tries left, or there are no bricks left on the screen, the
        game is over and it switches to STATE_INACTIVE.  All of these checks
        should be in Gameplay, NOT in this class.
        
        You are allowed to add more states if you wish. Should you do so,
        you should describe them here.
        
        Precondition: dt is the time since last update (a float).  This
        parameter can be safely ignored. It is only relevant for debugging
        if your game is running really slowly. If dt > 0.5, you have a 
        framerate problem because you are trying to do something too complex."""
        
        if self._state == STATE_COMPLETE:
            self._game = Gameplay()
            if self.view.touch is not None:
                self._lives = 3
                self._time = 0
                self._game = Gameplay()
                self._state = STATE_COUNTDOWN
        
        self._startCountdownIf()
        if self._state == STATE_COUNTDOWN:
            self._performCountdown()
        
        if self._state == STATE_ACTIVE:
            self._game.updatePaddle(self.view)
            self._game.updateBall()
            
        if self._state == STATE_ACTIVE and self.livesLost():
            if self._lives == 0:
                self._state = STATE_COMPLETE
            else:
                self._state = STATE_PAUSE
                self._paused_at = time.time()
            
        if self._state == STATE_PAUSE:
            #check how long its been paused
            if self.view.touch is not None:
                if time.time() - self._paused_at > 1:
                    self._state = STATE_ACTIVE
                    
        if self._state == STATE_ACTIVE and (self._game._wall.getBricks() == [] or self._lives == 0):
            self._state = STATE_COMPLETE
            
        
        
                
        
                    
    
    def draw(self):
        """Draws the game objects to the view.
        
        Every single thing you want to draw in this game is a GObject. 
        To draw a GObject g, simply use the method g.draw(view).  It is 
        that easy!
        
        Many of the GObjects (such as the paddle, ball, and bricks) are
        attributes in Gameplay. In order to draw them, you either need to
        add getters for these attributes or you need to add a draw method
        to class Gameplay.  We suggest the latter.  See the example 
        subcontroller.py from class."""
        
        if self._game != None:
            self._game.draw(self.view)
        
        self._welcome_message.draw(self.view)
        
        if self._state == STATE_COUNTDOWN:
            self._welcome_message = GLabel(x=100,y=250,
                                           text='Get Ready',font_size=50,
                                           halign='left',valign='bottom',
                                           linecolor=colormodel.RGB(0,76,153), bold=True)
        if self._state == STATE_ACTIVE:
            self._welcome_message = GLabel(text='')
        
        if self._state == STATE_PAUSE and self._lives == 2:
            self._pause_message1.draw(self.view)
            self._get_new_message.draw(self.view)
        elif self._state == STATE_PAUSE and self._lives == 1:
            self._pause_message2.draw(self.view)
            self._get_new_message.draw(self.view)
        elif self._state == STATE_COMPLETE and self._lives == 0:
            self._gameOver_message.draw(self.view)
            self._newGame_message.draw(self.view)
        elif self._state == STATE_ACTIVE and self._game._wall.getBricks() == []:
            self._youWin_message.draw(self.view)
            self._newGame_message.draw(self.view)
            
            
            
    
    # HELPER METHODS FOR THE STATES GO HERE
    
    
    def _startCountdownIf(self):
        """Changes state upon detecting touch"""
        
        if self._last is None and self.view.touch is not None:
            self._last = self.view.touch
            self._state = STATE_COUNTDOWN
            self._game = Gameplay()

            
            
    def _performCountdown(self):
        """Performs the countdown to start the game. """
        
        #increment ellapsed time by 16 until 3000 (3 seconds)
        self._time = self._time + 1
        if self._time >= 180:
            self._state = STATE_ACTIVE
            
    
    def livesLost(self):
        """Delete ball if it hits the floor, update lives"""
        
        if self._game._ball.y <= 0:
            self._game._ball = Ball()
            self._lives = self._lives - 1
            return True
        
    def livesLost(self):
        """Delete ball if it hits the floor, update lives"""
        
        if self._game._ball.y <= 0:
            self._game._ball = Ball()
            self._lives = self._lives - 1
            return True