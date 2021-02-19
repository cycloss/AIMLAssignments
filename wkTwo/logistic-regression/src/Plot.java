import org.knowm.xchart.*;
import org.knowm.xchart.style.markers.SeriesMarkers;

import javax.swing.*;
import java.awt.*;
import java.util.Collections;
import java.util.List;

public class Plot {

    XYChart chart;
    double yMin;
    double yMax;
    double xMin;
    double xMax;
    JFrame frame;

    public Plot(String title, String xAxis, String yAxis, List<List<Double>> data) {
        // Create the chart
        chart = new XYChartBuilder().width(1000).height(600).title(title).xAxisTitle(xAxis).yAxisTitle(yAxis).build();

        // Finding the domain and range to plot the graph in
        this.yMin = yMin(data);
        this.yMax = yMax(data);
        this.xMin = xMin(data);
        this.xMax = xMax(data);

        // Set the domain and range of the graph.
        chart.getStyler().setYAxisMin(yMin);
        chart.getStyler().setYAxisMax(yMax);
        chart.getStyler().setXAxisMin(xMin);
        chart.getStyler().setXAxisMax(xMax);

        // Create the scatter plot of the data
        XYSeries raw = chart.addSeries("raw", data.get(0), data.get(2));
        raw.setXYSeriesRenderStyle(XYSeries.XYSeriesRenderStyle.Scatter);

        // Plot the initial decision boundary with multiple points and join them with a
        // line
        List<List<Double>> plotPoints = Data.plotFunction(xMin, xMax, .1, (x1) -> 1);

        // To draw the decision boundary's initial point.
        XYSeries plt = chart.addSeries("plot", plotPoints.get(0), plotPoints.get(1));
        plt.setXYSeriesRenderStyle(XYSeries.XYSeriesRenderStyle.Line);
        plt.setShowInLegend(false);
        plt.setMarker(SeriesMarkers.NONE);

        SwingUtilities.invokeLater(() -> {

            // Create and set up the window.
            frame = new JFrame(title);
            frame.setLayout(new BorderLayout());
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

            // chart
            JPanel chartPanel = new XChartPanel<>(chart);
            frame.add(chartPanel, BorderLayout.CENTER);

            // Display the window.
            frame.pack();
            frame.setVisible(true);
        });
    }

    double yMin(List<List<Double>> data) {
        double min = Collections.min(data.get(2));
        return (min >= 0) ? 0 : min;
    }

    double yMax(List<List<Double>> data) {
        return Collections.max(data.get(2));
    }

    double xMin(List<List<Double>> data) {
        double min = Collections.min(data.get(0));
        return (min >= 0) ? 0 : min;
    }

    double xMax(List<List<Double>> data) {
        return Collections.max(data.get(0));
    }

    public void updatePlot(DecisionBoundary h_x) {
        List<List<Double>> plotPoints = Data.plotFunction(xMin, xMax, .1, h_x);
        chart.updateXYSeries("plot", plotPoints.get(0), plotPoints.get(1), null);
        frame.repaint();
    }

}
