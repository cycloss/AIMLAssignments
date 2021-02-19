import java.util.List;

public class GradientDescentNonLinear {

    public static void main(String[] args) {

        if (args.length != 1) {
            System.out.println("Please provide a data file to fun data with");
            return;
        }

        // -------------------------------------------------
        // Data and Graph setup.
        // -------------------------------------------------
        List<List<Double>> data = Data.dataFrom(args[0]);
        Plot plt = new Plot("Non linear test", "Independent", "Dependent", data);
        sleep(500);

        // -------------------------------------------------
        // Gradient Descent
        // -------------------------------------------------
        final int epochs = 100000; // Number of iterations we want to run through the algorithm
        // We want to predict hw( x ) = w0 + w1x + w2x^2
        System.out.println("Running " + epochs + " epochs...");
        double w0 = 0;
        double w1 = 0;
        double w2 = 0;

        // Learning rate
        double alpha = 0.00000001;

        // Main Gradient Descent Function for Linear Regression
        double epochCost = 0;
        for (int i = 0; i < epochs; i++) {

            double cost = 0;

            for (int j = 0; j < data.get(0).size(); j++) {

                double x_j = data.get(0).get(j);
                double y_j = data.get(1).get(j);

                // We want to predict hw( x ) = w0 + w1x + w2x^2
                double prediction = (w1 * x_j) + w0 + (w2 * (Math.pow(x_j, 2)));

                // cost += (y_j - h(x))^2
                cost += Math.pow((y_j - prediction), 2);

                // Update the parameters for our equation.

                w0 += alpha * (y_j - prediction);
                w1 += alpha * (y_j - prediction) * x_j;
                w2 += alpha * (y_j - prediction) * Math.pow(x_j, 2);
            }
            epochCost = cost;
            // double avCost = cost / data.get(0).size();
            // System.out.println("Current Cost: " + avCost);

            // ---------------------------------------------
            // Our Hypothesis Function after the epoch
            // (these values are final because of how
            // functional programming works in Java).

            final double w_0 = w0;
            final double w_1 = w1;
            final double w_2 = w2;
            HypothesisFunction h_x = (x) -> w_0 + (w_1 * x) + (w_2 * Math.pow(x, 2));
            // ----------------------------------------------
            // Plotting prediction with current values of w
            plt.updatePlot(h_x);
            // sleep(10);
            // ----------------------------------------------
        }
        String equation = String.format("Final Equation: h(x) = %.5f + (%.5f * x) + (%.5f * x^2)", w0, w1, w2);
        System.out.println(equation);
        double avCost = epochCost / data.get(0).size();
        System.out.println("Final Cost: " + avCost);
    }

    static void sleep(int ticks) {
        try {
            Thread.sleep(ticks);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
