class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        x_ax = min(C, G) - max(A, E)
        y_ax = min(D, H) - max(B, F)
        total = (C-A)*(D-B) + (G-E)*(H-F)
        if x_ax < 0 or y_ax < 0: #no overlap
            return total
        else:
            return total - x_ax*y_ax

# Find the total area covered by two rectilinear rectangles in a 2D plane.
# Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
# Example:
# Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
# Output: 45
# Assume that the total area is never beyond the maximum possible value of int.