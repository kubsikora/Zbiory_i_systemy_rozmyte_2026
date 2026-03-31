import fuzzlib.FuzzySet;
import fuzzlib.creators.OperationCreator;
import fuzzlib.norms.SNorm;
import fuzzlib.norms.TNorm;

public class Zad5 {
    public static void main(String[] args) {

        double sensorLight = 30.0;
        double sensorMotion = 1.0;

        System.out.println("Input: L=" + sensorLight + ", M=" + sensorMotion);

        FuzzySet lightLow = new FuzzySet(); lightLow.newTriangle(0, 50);
        FuzzySet lightMid = new FuzzySet(); lightMid.newTriangle(50, 50);
        FuzzySet lightHigh = new FuzzySet(); lightHigh.newTriangle(100, 50);

        FuzzySet motionNone = new FuzzySet(); motionNone.newTriangle(0, 1);
        FuzzySet motionActive = new FuzzySet(); motionActive.newTriangle(1, 1);

        FuzzySet outBrightLow = new FuzzySet(); outBrightLow.newTriangle(0, 50);
        FuzzySet outBrightMid = new FuzzySet(); outBrightMid.newTriangle(50, 50);
        FuzzySet outBrightHigh = new FuzzySet(); outBrightHigh.newTriangle(100, 50);

        FuzzySet durationShort = new FuzzySet(); durationShort.newTriangle(10, 20);
        FuzzySet durationMid = new FuzzySet(); durationMid.newTriangle(40, 30);
        FuzzySet durationLong = new FuzzySet(); durationLong.newTriangle(80, 40);

        double[] rW = {
            Math.min(lightLow.getMembership(sensorLight), motionNone.getMembership(sensorMotion)),
            Math.min(lightLow.getMembership(sensorLight), motionActive.getMembership(sensorMotion)),
            Math.min(lightMid.getMembership(sensorLight), motionNone.getMembership(sensorMotion)),
            Math.min(lightMid.getMembership(sensorLight), motionActive.getMembership(sensorMotion)),
            Math.min(lightHigh.getMembership(sensorLight), motionNone.getMembership(sensorMotion)),
            Math.min(lightHigh.getMembership(sensorLight), motionActive.getMembership(sensorMotion))
        };

        FuzzySet[] targetBrightness = {
            outBrightLow, outBrightHigh,
            outBrightLow, outBrightMid,
            outBrightLow, outBrightLow
        };

        FuzzySet[] targetDuration = {
            durationShort, durationLong,
            durationShort, durationMid,
            durationShort, durationShort
        };

        TNorm tMin = OperationCreator.newTNorm(TNorm.TN_MINIMUM);
        SNorm sMax = (SNorm) OperationCreator.newSNorm(SNorm.SN_MAXIMUM);

        FuzzySet resBrightness = new FuzzySet();
        resBrightness.addPoint(0, 0);
        resBrightness.addPoint(100, 0);

        FuzzySet resDuration = new FuzzySet();
        resDuration.addPoint(0, 0);
        resDuration.addPoint(100, 0);

        for (int i = 0; i < rW.length; i++) {
            if (rW[i] <= 0) continue;

            FuzzySet weightSet = new FuzzySet();
            weightSet.addPoint(0, rW[i]);
            weightSet.addPoint(100, rW[i]);

            FuzzySet cutB = new FuzzySet();
            FuzzySet cutD = new FuzzySet();

            FuzzySet.processSetsWithNorm(cutB, targetBrightness[i], weightSet, tMin);
            FuzzySet.processSetsWithNorm(cutD, targetDuration[i], weightSet, tMin);

            FuzzySet nextB = new FuzzySet();
            FuzzySet nextD = new FuzzySet();

            FuzzySet.processSetsWithNorm(nextB, resBrightness, cutB, sMax);
            FuzzySet.processSetsWithNorm(nextD, resDuration, cutD, sMax);

            resBrightness = nextB;
            resDuration = nextD;
        }

        long finalBright = Math.round(resBrightness.DeFuzzyfy());
        long finalDuration = Math.round(resDuration.DeFuzzyfy());

        System.out.println("Brightness: " + finalBright + "%");
        System.out.println("Duration: " + finalDuration + "s");
    }
}