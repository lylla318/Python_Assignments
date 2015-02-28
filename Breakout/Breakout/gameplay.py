# gameplay.py
# LYLLA YOUNES, LEY23
# DATE COMPLETED HERE
"""Subcontroller module for Breakout

This module contains the subcontroller to manage a single game in the Breakout App. 
Instances of Gameplay represent a single game.  If you want to restart a new game,
you are expected to make a new instance of Gameplay.

The subcontroller Gameplay manages the paddle, ball, and bricks.  These are model
objects.  The ball and the bricks are represented by classes stored in models.py.
The paddle does not need a new class (unless you want one), as it is an instance
of GRectangle provided by game2d.py.

Most of your work on this assignment will be in either this module or models.py.
Whether a helper method belongs in this module or models.py is often a complicated
issue.  If you do not know, ask on Piazza and we will answer."""
from constants import *
from game2d import *
from models import *

fixed_point = None

# PRIMARY RULE: Gameplay can only access attributes in models.py via getters/setters
# Gameplay is NOT allowed to access anything in breakout.py (Subcontrollers are not
# permitted to access anything in their parent. To see why, take CS 3152)


class Gameplay(object):
    """An instance controls a single game of breakout.
    
    This subcontroller has a reference to the ball, paddle, and bricks. It
    animates the ball, removing any bricks as necessary.  When the game is
    won, it stops animating.  You should create a NEW instance of 
    Gameplay (in Breakout) if you want to make a new game.
    
    If you want to pause the game, tell this controller to draw, but do not
    update.  See subcontrollers.py from Lecture 24 for an example.
    
    INSTANCE ATTRIBUTES:
        _wall   [BrickWall]:  the bricks still remaining 
        _paddle [GRectangle]: the paddle to play with 
        _ball [Ball, or None if waiting for a serve]: 
            the ball to animate
        _last [GPoint, or None if mouse button is not pressed]:  
            last mouse position (if Button pressed)
        _tries  [int >= 0]:   the number of tries left
        _last_pos [GPoint, or None is mouse button is not pressed]
            position of a click while the game is underway
    
    As you can see, all of these attributes are hidden.  You may find that you
    want to access an attribute in call Breakout. It is okay if you do, but
    you MAY NOT ACCESS THE ATTRIBUTES DIRECTLY. You must use a getter and/or
    setter for any attribute that you need to access in Breakout.  Only add
    the getters and setters that you need for Breakout.
    
    You may change any of the attributes above as you see fit. For example, you
    might want to make a Paddle class for your paddle.  If you make changes,
    please change the invariants above.  Also, if you add more attributes,
    put them and their invariants below.
                  
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    
    _fixed_point [GPoint, or None if the mouse button is not pressed]
        fixed position of user's mouse
    
    """
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)*******
    
    
    # INITIALIZER (standard form) TO CREATE PADDLES AND BRICKS
    
    def __init__(self):
        """ Initializer for Gameplay   """
        
        self._wall = BrickWall()
        self._paddle = GRectangle(center_x = GAME_WIDTH/2, y = PADDLE_OFFSET,
        width = PADDLE_WIDTH, height = PADDLE_HEIGHT,
        fillcolor = colormodel.BLACK,linecolor = colormodel.BLACK )
        self._ball = Ball()
        self._last = None
        self._tries = 0
        self._last_pos = None
        self._fixed_point = None
        self._saucerSound = Sound('saucer1.wav')
        self._cupSound = Sound('cup1.wav')
        
        
    
    # DRAW METHOD TO DRAW THE PADDLES, BALL, AND BRICKS
        
    def draw(self, view):
        """ Draws instance of a single game in Breakout """
        self._wall.draw(view)
        self._paddle.draw(view)
        #need to see if ball is there
        if self._ball is not None:
            self._ball.draw(view)
        
    
    
    # UPDATE METHODS TO MOVE PADDLE, SERVE AND MOVE THE BALL
    
    def inside_paddle(self, view):
        """This method checks if the user clicks inside the paddle"""
        click_point = view.touch
        
        if click_point.x >= self._paddle.x and click_point.x <= (self._paddle.x+BRICK_WIDTH):
            if click_point.y >= self._paddle.y and click_point.y <= (self._paddle.y + BRICK_HEIGHT):
                return True
        else:
            return False
    
            
            
    def touch_down(self, view):
        """Helper function for updatePaddle: determines what to do if
        user is pressing mouse."""
        
        if view.touch is not None:
            if self.inside_paddle(view):
                self._fixed_point = view.touch #set fixed_point to where user pressed
    
    
    def moving_touch(self, view):
        """Helper function for updatePaddle: determines what to do if
        user is moving mouse."""
        
        current_touch = view.touch
        
        if current_touch is not None and self._fixed_point is not None:
            self._paddle.x = self._paddle.x + current_touch.x - self._fixed_point.x
            self._fixed_point.x = current_touch.x  
            
            
    def no_touch(self, view):
        """Helper function for updatePaddle: determines what to do if
        user is not pressing mouse."""
        
        if view.touch is None:
            self._fixed_point = None
    
    
    def updatePaddle(self,view):
        """Updates paddle object"""
        self.touch_down(view)
        self.moving_touch(view)
        self.no_touch(view)
        
    def updateBall(self):
        """Updates ball object"""
        self._ball.moveBall()
        
        if self._getCollidingObject() == self._paddle:
            self._ball._vy = -(self._ball._vy)
            self._cupSound.play()
        elif self._getCollidingObject() in self._wall.getBricks():
            self._ball._vy = -(self._ball._vy)
            self._wall.setBricks(self._getCollidingObject())
            self._saucerSound.play()


    def _getCollidingObject(self):
        """Returns: GObject that has collided with the ball
        This method checks the four corners of the ball, one at a
        time. If one of these points collides with either the paddle
        or a brick, it stops the checking immediately and returns the
        object involved in the collision. It returns None if no
        collision occurred. """
        
        #if ball hits paddle   
        if self._paddle.contains((self._ball.x + BALL_DIAMETER),self._ball.y) and self._ball._vy < 0:
            return self._paddle
        elif self._paddle.contains(self._ball.x,self._ball.y)and self._ball._vy < 0:
            return self._paddle
        elif self._paddle.contains(self._ball.x, (self._ball.y + BALL_DIAMETER))and self._ball._vy < 0:
            return self._paddle
        elif self._paddle.contains((self._ball.x + BALL_DIAMETER),
            (self._ball.y + BALL_DIAMETER))and self._ball._vy < 0:
            return self._paddle
    
        
        #if ball hits bricks
        for k in self._wall.getBricks():
            if k.contains((self._ball.x + BALL_DIAMETER),self._ball.y):
                return k
            elif k.contains(self._ball.x,self._ball.y):
                return k
            elif k.contains(self._ball.x, (self._ball.y + BALL_DIAMETER)):
                return k
            elif k.contains((self._ball.x + BALL_DIAMETER),
                (self._ball.y + BALL_DIAMETER)):
                return k
        
        return None
    
    
    
    
    
    
    # HELPER METHODS FOR PHYSICS AND COLLISION DETECTION
    
    # ADD ANY ADDITIONAL METHODS (FULLY SPECIFIED) HERE
    
