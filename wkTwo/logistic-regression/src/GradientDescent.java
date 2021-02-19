import java.util.List;

public class GradientDescent {

    public static void main(String[] args) {

        if (args.length != 1) {
            System.out.println("Please provide a data file to fun data with");
            return;
        }

        // -------------------------------------------------
        // Data and Graph setup.
        // -------------------------------------------------
        List<List<Double>> data = Data.dataFrom(args[0]);
        Plot plt = new Plot("Logistic test", "x1", "x2", data);
        sleep(1500);

        // -------------------------------------------------
        // Gradient Descent
        // -------------------------------------------------
        final int epochs = 1000; // Number of iterations we want to run through the algorithm

        System.out.println("Running " + epochs + " epochs...");
        double w0 = 0;
        double w1 = 0;
        double w2 = 0;

        // Learning rate
        double alpha = 0.2;

        // Main Gradient Descent Function for Logistic Regression
        double epochCost = 0;
        for (int i = 0; i < epochs; i++) {

            double cost = 0;

            for (int j = 0; j < data.get(0).size(); j++) {

                double x_j = data.get(0).get(j);
                double x2_j = data.get(2).get(j);
                double y_j = data.get(1).get(j);

                // z = hw( x ) = w0 + w1x + w2x2
                double z = w0 + (w1 * x_j) + (w2 * Math.pow(x2_j, 2));

                // sigmoided hypothesis: g(x) = 1 / 1 + e ^ -hwx
                double hypothesis = 1 / (1 + Math.exp(-z));

                // cost: if y is 1 and g(x) not 1
                double costIfYZero = (1 - y_j) * Math.log(1 - hypothesis);
                double costIfYOne = y_j * Math.log(hypothesis);
                float dataCount = data.get(0).size();
                cost += -(1 / dataCount) * (costIfYZero + costIfYOne);

                // Update the parameters for our equation.

                w0 += alpha * (y_j - hypothesis);
                w1 += alpha * (y_j - hypothesis) * x_j;
                w2 += alpha * (y_j - hypothesis) * Math.pow(x2_j, 2);
            }
            epochCost = cost;
            if (i % 10 == 0) {
                double avCost = cost / data.get(0).size();
                System.out.println("Current Cost: " + avCost);
            }
            final double w_0 = w0;
            final double w_1 = w1;
            final double w_2 = w2;

            // need the line equation for non linear:
            // y = mx^n + c)
            // By solving the general equation like:

            // set z equal zero, which will be ON the decision boundry
            // w1x1 + w2x2^2 + w0 = 0
            // then solve such that it's in the form y = mx + c, where y is the y axis
            // variable (x2)

            // Send both the w1x1 and w0 to the right side
            // w2x2^2 = -w1x1 - w0

            // divide both sides with w2
            // x2^2 = -w1x1 / w2 - w0 / w2
            // sqare root rhs
            // x2 = sqrt(-w1x1) - sqrt(w0 / w2)
            // now its in the form of y = mx + c

            // pass in x1 to get x2
            DecisionBoundary boundaryLine = (x1) -> Math.sqrt((-w_1 * x1 - w_0) / w_2);
            // ----------------------------------------------
            // Plotting prediction with current values of w
            plt.updatePlot(boundaryLine);
            sleep(10);
            // ----------------------------------------------
        }
        String equation = String.format("Final Decision Boundary: x2 = (%.10f * x1)^0.5 + %.5f", (-w1 / w2),
                Math.sqrt(-w0 / w2));
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
