from manim import *
import numpy as np


class SphereBySlicing(ThreeDScene):
    def construct(self):
        R = 2.5

        # Set up 3D axes
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-3, 3, 1],
        )
        self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES)

        self.play(Create(axes))

        # Sphere surface (for reference)
        sphere = Sphere(radius=R, resolution=(24, 24))
        sphere.set_fill(BLUE_E, opacity=0.15)
        sphere.set_stroke(BLUE, opacity=0.4)

        self.play(FadeIn(sphere))

        # Function for radius of slice at x
        def slice_radius(x):
            return np.sqrt(max(0, R**2 - x**2))

        # Create slices
        slices = VGroup()
        n_slices = 20  # increase this for smoother look
        xs = np.linspace(-R, R, n_slices)

        for x in xs:
            r = slice_radius(x)
            if r > 0:
                disk = Circle(radius=r, color=YELLOW)
                disk.set_fill(YELLOW, opacity=0.6)
                disk.rotate(PI / 2, axis=RIGHT)  # make it vertical
                disk.move_to(np.array([x, 0, 0]))
                slices.add(disk)

        # Animate slices appearing
        self.play(LaggedStart(*[FadeIn(d) for d in slices], lag_ratio=0.1, run_time=3))

        self.wait(1)

        # Increase number of slices for better approximation
        finer_slices = VGroup()
        n_slices_fine = 60
        xs_fine = np.linspace(-R, R, n_slices_fine)

        for x in xs_fine:
            r = slice_radius(x)
            if r > 0:
                disk = Circle(radius=r, color=ORANGE)
                disk.set_fill(ORANGE, opacity=0.5)
                disk.rotate(PI / 2, axis=RIGHT)
                disk.move_to(np.array([x, 0, 0]))
                finer_slices.add(disk)

        self.play(Transform(slices, finer_slices), run_time=3)

        self.wait(2)
