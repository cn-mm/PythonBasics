[OpenCV tutorials](https://pythonprogramming.net/loading-images-python-opencv-tutorial/) by [Sentdex](https://pythonprogramming.net/)

Image Detection and Video Detection paradigms are very similar.

**Stuff that can be done using opencv:**
1. Background Subtracting
2. Edge Detection
3. Colour Filtering
4. Feature Matching
5. General object recognition 

> Pixel Values in the case of edge detection:
>  - Black : (0,0,0)
>  - White : (255,255,255)

IMREAD_COLOR : default, color without any alpha channel (**alpha is the degree of opaqueness**)
IMREAD_UNCHANGED : retains the alpha channel

In case of cv2 we have BGR and with alpha channel we have BGRA

> Colors as numbers:
>   - Color (IMREAD_COLOR) is 1  
>   - Graysvale (IMREAD_GRAYSCALE) is 0 (much more simplified)
>   - Unchanged (IMREAD_UNCHANGED) is -1

Image analysis and video analysis in full color would require a lot more processing.

Can show the image using either
1. cv2 (Does BGR)
2. matpotlib (Does RGB)
