//
// Decompiled by CFR - 1788ms
//
package com.SDE;

import android.app.AppGlobals;
import android.app.Application;
import android.content.Context;
import android.os.Environment;
import android.widget.Toast;
import com.Fix.Pref;
import com.Helper;
import com.SDE.GetMenuValues;
import com.SDE.getGammaCurve;
import com.SDE.getToneCurve;
import java.io.BufferedInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.RandomAccessFile;
import java.io.Serializable;

/*
 * Exception performing whole class analysis ignored.
 */
public class LibPatcher {
    public static int A = 0;
    private static final int FILE_WRITE_BUFFER_SIZE = 32256;
    private static final int _AVGLDR = 0x0298390c;
    private static final int _AppDiGainSet = 0x011e6a38;
    private static final int _BY = 3586320;
    private static final int _BayerNModHal1 = 0x028cbf04;
    private static final int _BetterColWiener = 0x02cf41a8;
    private static final int _BlackLevel = 0x0111f258;
    private static final int _BlurPreview = 0x011e3b50;
    private static final int _BrightN = 0x02912054;
    private static final int _Brightnessintensity = 0x0299d36c;
    private static final int _CContrast = 0x020f24a8;
    private static final int _CContrast2 = 0x01ff8444;
    private static final int _CG10 = 0x0297ba58;
    private static final int _CG2 = 0x0297ba2c;
    private static final int _CG3 = 0x0297ba44;
    private static final int _CG4 = 0x0297ba5c;
    private static final int _CG5 = 0x0297ba7c;
    private static final int _CG6 = 0x0297baa8;
    private static final int _CG9 = 0x0297ba40;
    private static final int _ChromaA = 0x01fbc950;
    private static final int _ChromaB = 0x01fbc954;
    private static final int _Clarity = 0x01fbf724;
    private static final int _CoefSabrTuNoise = 3552444;
    private static final int _ColProcessing = 0x01fbe110;
    private static final int _Contr = 0x02b823e4;
    private static final int _Contrast4 = 0x02984af8;
    private static final int _Contrast5 = 0x02984b04;
    private static final int _ContrastBlack = 3560676;
    private static final int _ContrastL1 = 3558880;
    private static final int _ContrastL2 = 3562224;
    private static final int _ContrastL3a = 0x02b823b8;
    private static final int _Darkenlight = 0x02ca25d0;
    private static final int _Darker = 0x029c551c;
    private static final int _DehazeBlack = 0x01ff795c;
    private static final int _DehazedExpo = 0x01fbc9ec;
    private static final int _Dehazedregulator2 = 0x01fbf354;
    private static final int _DenSmoothing1 = 0x02cf4cf8;
    private static final int _DenSmoothing2 = 0x02cf40e8;
    private static final int _Denoise = 0x01fbc5d8;
    private static final int _Depth1 = 0x02b9832c;
    private static final int _Depth2 = 0x02b98330;
    private static final int _DiscardFramesWithTetMismatch = 0x01ee6fac;
    private static final int _ExpoComp = 0x02987e28;
    private static final int _ExpoCor = 0x0298387c;
    private static final int _Exposition = 0x02979d48;
    private static final int _Exposure = 0x029846b8;
    private static final int _ExposureDarker = 0x02ca1a54;
    private static final int _ExposureDarker2 = 0x02ca1b10;
    private static final int _FixNoiseSabre = 0x028138e0;
    private static final int _FixRaw16Merge = 0x02811080;
    private static final int _FixShastaMerge = 0x02813580;
    private static final int _GRO = 3586328;
    private static final int _Green = 3560920;
    private static final int _HDR2 = 0x01ff8324;
    private static final int _HDRBrightness = 0x020f22f4;
    private static final int _HDREffect = 0x020ecab0;
    private static final int _HDREffectInt = 0x020ef26c;
    private static final int _HDRModel = 0x02ca7e58;
    private static final int _HDROverLight = 0x020ec92c;
    private static final int _HDRRangeMinus = 0x029884ac;
    private static final int _HDRRangePlus = 0x029884b8;
    private static final int _HDRRatio2 = 0x02979c9c;
    private static final int _HDRRatio3 = 0x02986d10;
    private static final int _HDRRaw2 = 0x0299d70c;
    private static final int _HDRSabreCalcVal1 = 0x02cf71cc;
    private static final int _HDRSabreCalcVal2 = 0x02cf740c;
    private static final int _HardJPGQuality = 0x02a81a1c;
    private static final int _HardMerge = 0x011eb1a8;
    private static final int _HdrPlusInterface = 0x01ec0908;
    private static final int _Hightlight2 = 0x0298502c;
    private static final int _HightlightCompensation2 = 0x020ee2ac;
    private static final int _Hotpixelsuppres = 0x01fc3edc;
    private static final int _ISO = 0x02974500;
    private static final int _InitParams = 0x011ea6a4;
    private static final int _InitParams2 = 0x011ea6b8;
    private static final int _InitParams_1simultaneous_1merge_1and_1finish_1set = 0x011ea6d4;
    private static final int _IsoExpoTun = 0x02a5d620;
    private static final int _LDR = 0x0299cf40;
    private static final int _LibSignature = 2174870;
    private static final int _Light = 0x020ee320;
    private static final int _LightFix = 2018912;
    private static final int _LightFix2 = 0x029866e8;
    private static final int _LightFix3 = 0x01ecdf8c;
    private static final int _Lighting = 0x0280bbe8;
    private static final int _LumaA = 0x01fbc77c;
    private static final int _LumaB = 0x01fbc780;
    private static final int _LumaDHL1 = 11537011;
    private static final int _LumaDHL2 = 11537028;
    private static final int _LumaDHL3 = 11537045;
    private static final int _LumaDHL4 = 11537062;
    private static final int _LumaDHL5 = 11537079;
    private static final int _LumaDHSL1 = 11537299;
    private static final int _LumaDHSL2 = 11537284;
    private static final int _LumaDHSL3 = 0xB00BB5;
    private static final int _LumaDHSL4 = 11537350;
    private static final int _LumaDHSL5 = 11537367;
    private static final int _LumaDHSabreL1 = 11520963;
    private static final int _LumaDHSabreL1A = 11520968;
    private static final int _LumaDHSabreL1B = 11520973;
    private static final int _LumaDHSabreL2 = 11520980;
    private static final int _LumaDHSabreL2A = 11520985;
    private static final int _LumaDHSabreL2B = 11520990;
    private static final int _LumaDHSabreL3 = 11520997;
    private static final int _LumaDHSabreL3A = 11521002;
    private static final int _LumaDHSabreL3B = 11521007;
    private static final int _LumaDHSabreL4 = 11521014;
    private static final int _LumaDHSabreL4A = 11521019;
    private static final int _LumaDHSabreL4B = 11521024;
    private static final int _LumaDHSabreL5 = 11521031;
    private static final int _LumaDHSabreL5A = 11521036;
    private static final int _LumaDLL1 = 11537107;
    private static final int _LumaDLL2 = 11537124;
    private static final int _LumaDLL3 = 11537141;
    private static final int _LumaDLL4 = 0xB00B06;
    private static final int _LumaDLL5 = 11537175;
    private static final int _LumaDLSL1 = 11537379;
    private static final int _LumaDLSL2 = 11537396;
    private static final int _LumaDLSL3 = 11537413;
    private static final int _LumaDLSL4 = 11537430;
    private static final int _LumaDLSL5 = 11537447;
    private static final int _LumaDLSabreL1 = 11521059;
    private static final int _LumaDLSabreL1A = 11521064;
    private static final int _LumaDLSabreL1B = 11521069;
    private static final int _LumaDLSabreL2 = 11521076;
    private static final int _LumaDLSabreL2A = 11521081;
    private static final int _LumaDLSabreL2B = 11521086;
    private static final int _LumaDLSabreL3 = 11521093;
    private static final int _LumaDLSabreL3A = 11521098;
    private static final int _LumaDLSabreL3B = 11521103;
    private static final int _LumaDLSabreL4 = 11521110;
    private static final int _LumaDLSabreL4A = 11521115;
    private static final int _LumaDLSabreL4B = 11521120;
    private static final int _LumaDLSabreL5 = 11521127;
    private static final int _LumaDLSabreL5A = 11521132;
    private static final int _LumaDML1 = 0xB00B33;
    private static final int _LumaDML2 = 0xB00B44;
    private static final int _LumaDML3 = 0xB00B55;
    private static final int _LumaDML4 = 0xB00B66;
    private static final int _LumaDML5 = 0xB00B77;
    private static final int _LumaDMSL1 = 11537475;
    private static final int _LumaDMSL2 = 11537492;
    private static final int _LumaDMSL3 = 11537509;
    private static final int _LumaDMSL4 = 11537526;
    private static final int _LumaDMSL5 = 11537543;
    private static final int _LumaDMSabreL1 = 11521155;
    private static final int _LumaDMSabreL1A = 11521160;
    private static final int _LumaDMSabreL1B = 11521165;
    private static final int _LumaDMSabreL2 = 11521172;
    private static final int _LumaDMSabreL2A = 11521177;
    private static final int _LumaDMSabreL2B = 11521182;
    private static final int _LumaDMSabreL3 = 11521189;
    private static final int _LumaDMSabreL3A = 0xAFCCAA;
    private static final int _LumaDMSabreL3B = 0xAFCCAF;
    private static final int _LumaDMSabreL4 = 11521206;
    private static final int _LumaDMSabreL4A = 11521211;
    private static final int _LumaDMSabreL4B = 11521216;
    private static final int _LumaDMSabreL5 = 11521223;
    private static final int _LumaDMSabreL5A = 0xAFCCCC;
    private static final int _LumaDNewA = 0x02cf83f0;
    private static final int _LumaDNewB = 0x02cf83f4;
    private static final int _LumaDenoise = 0x01ff6c74;
    private static final int _LumaNew = 0x02cf8460;
    private static final int _LumaNoise = 0x02cf7040;
    private static final int _LumaNoise1 = 0x01fbcf74;
    private static final int _LumaSmooth = 0x01fc1c28;
    private static final int _LutNoiseFix = 0x02c9eec4;
    private static final int _MaxRelativeTetFactor = 0x02971f78;
    private static final int _NContrast1 = 0x01ff7b10;
    private static final int _NROpacity = 0x01fbe49c;
    private static final int _NightModeExposition = 0x02979d40;
    private static final int _NightModeGain = 0x02974548;
    private static final int _NoiseModelShot = 0x02cf58c4;
    private static final int _NoiseModelUnblock = 0x01ecf69c;
    private static final int _NoiseReductA0 = 0x0111e2f4;
    private static final int _NoiseReductA1 = 0x0111e2f0;
    private static final int _NoiseReductA2 = 0x0111e30c;
    private static final int _NoiseReductSabre = 0x02813220;
    private static final int _NoiseReductSabre1 = 0x02813218;
    private static final int _Noisemodel = 0x01fdd638;
    private static final int _ORGB = 3586332;
    private static final int _RaisrZFTuning1 = 3588720;
    private static final int _RaisrZFTuning2 = 3588724;
    private static final int _RawCompress = 0x011eaee4;
    private static final int _RecomputeWBOnBaseFrame = 0x011eae28;
    private static final int _Red = 3560924;
    private static final int _ResamplMethod = 0x01edd91c;
    private static final int _Robustness = 3276325;
    private static final int _SABRE1 = 0x0280e170;
    private static final int _SABRE2 = 0x0280e1ec;
    private static final int _SABRE3 = 0x0280e1f0;
    private static final int _SabrBurMerge1 = 0x02812d58;
    private static final int _SabrBurMerge2 = 0x02812d60;
    private static final int _SabrBurMerge3 = 0x02812d74;
    private static final int _SabreBM1 = 0x02813658;
    private static final int _SabreBM2 = 0x02813660;
    private static final int _SabreBM3 = 0x02813664;
    private static final int _SabreByRAWToYUV = 0x02cf51c8;
    private static final int _SabreContrast = 0x02910bdc;
    private static final int _SabreContrastSharp = 0x02910bcc;
    private static final int _SabreLNewL1 = 11507060;
    private static final int _SabreLNewL2 = 11507072;
    private static final int _SabreLNewL3 = 11507084;
    private static final int _SabreLNewL4 = 11507096;
    private static final int _SabreLNewL5 = 11507108;
    private static final int _SabreLNewNL1 = 11507168;
    private static final int _SabreLNewNL2 = 11507180;
    private static final int _SabreLNewNL3 = 11507192;
    private static final int _SabreLNewNL4 = 11507204;
    private static final int _SabreLNewNL5 = 11507216;
    private static final int _SabreLNewNL6 = 11507228;
    private static final int _SabreLNewNL7 = 11507240;
    private static final int _SabreLNewNL8 = 11507252;
    private static final int _SabreLNewNL9 = 11507264;
    private static final int _SabreNoiseArt = 0x02813648;
    private static final int _SabreNoiseEstimals = 0x02812374;
    private static final int _SabreSharp = 11507144;
    private static final int _SabreSharp2 = 0x01ede564;
    private static final int _SabreSharp3 = 0x0280c468;
    private static final int _Sat4 = 0x02b8241c;
    private static final int _Saturation = 0x01fbca80;
    private static final int _Saturation2 = 0x0297b9f0;
    private static final int _Saturation3 = 0x01fbf074;
    private static final int _SavMergChrDen = 0x02819224;
    private static final int _SensorID = 0x01ef809c;
    private static final int _ShadowCompensation = 0x01fbdaa8;
    private static final int _ShadowTuning = 0x01fe0390;
    private static final int _SharpDRad1 = 0x01fc3dc0;
    private static final int _SharpDRad2 = 0x01fc3dd8;
    private static final int _SharpGain = 0x01fbc294;
    private static final int _SharpGainMacro = 0x01fbc3bc;
    private static final int _SharpGainMicro = 0x01fbc328;
    private static final int _SharpMacro = 11507156;
    private static final int _SharpMini = 11507132;
    private static final int _SharpShastaMotion = 0x0299db74;
    private static final int _SharpenHighL1 = 11537715;
    private static final int _SharpenHighL2 = 11537727;
    private static final int _SharpenHighL3 = 11537739;
    private static final int _SharpenHighWL1 = 11537955;
    private static final int _SharpenHighWL2 = 11537967;
    private static final int _SharpenHighWL3 = 11537979;
    private static final int _SharpenLowL1 = 11537619;
    private static final int _SharpenLowL2 = 11537631;
    private static final int _SharpenLowL3 = 11537643;
    private static final int _SharpenLowWL1 = 11537859;
    private static final int _SharpenLowWL2 = 11537871;
    private static final int _SharpenLowWL3 = 0xB00DDB;
    private static final int _SharpenMediumL1 = 11537411;
    private static final int _SharpenMediumL2 = 11537423;
    private static final int _SharpenMediumL3 = 11537435;
    private static final int _SharpenMediumWL1 = 11537907;
    private static final int _SharpenMediumWL2 = 11537919;
    private static final int _SharpenMediumWL3 = 0xB00E0B;
    private static final int _SharpenVeryLowL1 = 11537571;
    private static final int _SharpenVeryLowL2 = 11537583;
    private static final int _SharpenVeryLowL3 = 0xB00CBB;
    private static final int _SharpenVeryLowWL1 = 11537811;
    private static final int _SharpenVeryLowWL2 = 11537823;
    private static final int _SharpenVeryLowWL3 = 11537835;
    private static final int _SharpeningEdge = 0x01fbec90;
    private static final int _SharpnessA = 0x01fbc1f8;
    private static final int _SharpnessB = 0x01fbc1fc;
    private static final int _SharpnessNoiseModel = 0x0283c238;
    private static final int _ShastaFactor = 0x011eb2dc;
    private static final int _ShastaForce = 0x011eb2c8;
    private static final int _ShotNoiseFactor = 0x02cf5740;
    private static final int _ShotParams_1allow_1base_1frame_1reuse_1set = 0x011eb15c;
    private static final int _ShotParams_1allow_1temporal_1binning_1set = 0x011eb12c;
    private static final int _ShotParams_1device_1is_1on_1tripod_1set = 0x011eb1e0;
    private static final int _ShotParams_1downsample_1by_12_1before_1merge_1set = 0x011eb314;
    private static final int _SkipMetadataCheck = 0x01ece754;
    private static final int _Smoothing1 = 0x027ff208;
    private static final int _Smoothing2 = 0x027ff29c;
    private static final int _SmoothingNew = 11507136;
    private static final int _SmoothingSabre = 11507120;
    private static final int _Smoothness = 0x01255fd4;
    private static final int _SoftContrast = 0x0298362c;
    private static final int _SoftSharpA = 0x01fbed44;
    private static final int _SoftSharpB = 0x01fbed48;
    private static final int _SoftSharpC = 0x01fbed88;
    private static final int _SpatialA = 0x01fbc8b4;
    private static final int _SpatialB = 0x01fbc8b8;
    private static final int _SpatialDenMi1 = 11527764;
    private static final int _SpatialDenMi2 = 11527768;
    private static final int _SpatialDenMi3 = 11527772;
    private static final int _SpatialDenMi4 = 11527776;
    private static final int _StartGamma = 11536120;
    private static final int _StartSect = 11535928;
    private static final int _StartTone = 11535984;
    private static final int _TemporalA = 0x01fbc818;
    private static final int _TemporalB = 0x01fbc81c;
    private static final int _TemporalBinning = 0x02961210;
    private static final int _TemporalDen = 0x011f1588;
    private static final int _TemporalRadius = 0x028417a4;
    private static final int _TunColSatPar1 = 3563912;
    private static final int _TunColSatPar2 = 3563916;
    private static final int _TunSupressHotPixel = 0x02974584;
    private static final int _Vignette = 0x02972fa8;
    private static final int _VignetteC = 0x02ca25e0;
    private static final int _VolumeProcessing1 = 0x020f0664;
    private static final int _VolumeProcessing2 = 0x020f0668;
    private static final int _WaveletLumaDenoiseSabreLevels = 11520963;
    private static final int _WhiteLevel = 0x01ff47f0;
    private static final int _YBP = 3617128;
    private static final int _Zipper1 = 3557400;
    private static final int _Zipper2 = 3557480;
    private static final int _Zipper3 = 3557484;
    public static String gammaPresetName;
    public static int sCamNum;
    public static String tonePresetName;
    private final char[] HEX_ARRAY = "0123456789ABCDEF".toCharArray();
    private String libName = "libpatched_jni.so";
    private boolean showToast = false;

    private static boolean applyPatcher(String string) {
        LibPatcher libPatcher = new LibPatcher();
        if (!libPatcher.moveLibToDir(string).equals("OK")) {
            return false;
        }
        LibPatcher.copySignature((LibPatcher)libPatcher);
        boolean bl = LibPatcher.copyLib((LibPatcher)libPatcher);
        if (Helper.MenuValue((String)"pref_save_patchedlib_key") != 0) {
            libPatcher.moveLibToDir2(string);
        }
        return bl;
    }

    private static boolean applyPatcherDisabled(String string) {
        LibPatcher libPatcher = new LibPatcher();
        if (!libPatcher.moveLibToDir(string).equals("OK")) {
            return false;
        }
        LibPatcher.copySignature((LibPatcher)libPatcher);
        boolean bl = LibPatcher.copyLibDisabled((LibPatcher)libPatcher);
        if (Helper.MenuValue((String)"pref_save_patchedlib_key") != 0) {
            libPatcher.moveLibToDir2(string);
        }
        return bl;
    }

    private String bytesToHex(byte[] byArray) {
        char[] cArray = new char[byArray.length * 2];
        for (int i = 0; i < byArray.length; ++i) {
            int n = byArray[i] & 0xFF;
            int n2 = i * 2;
            cArray[n2] = this.HEX_ARRAY[n >>> 4];
            cArray[n2 + 1] = this.HEX_ARRAY[n & 0xF];
        }
        return new String(cArray);
    }

    private static boolean copyLib(LibPatcher libPatcher) {
        boolean bl;
        if (GetMenuValues.getIntValue((String)Helper.SetLensValue((String)"lib_curve_key")) != 0) {
            libPatcher.setToneCurve();
        }
        if (GetMenuValues.getIntValue((String)Helper.SetLensValue((String)"lib_gamma_key")) != 0) {
            libPatcher.setGammaCurve();
        }
        libPatcher.setValueHex(_Contr, Helper.SetLensValue((String)"lib_contr_key"));
        libPatcher.setValueHex(_Sat4, Helper.SetLensValue((String)"lib_sat4_key"));
        libPatcher.setValueHex(_HightlightCompensation2, Helper.SetLensValue((String)"lib_hightlight2_key"));
        libPatcher.setValueHex(_TunSupressHotPixel, Helper.SetLensValue((String)"lib_tunsupresshotpixel_key"));
        libPatcher.setValueHex(_ShotParams_1device_1is_1on_1tripod_1set, Helper.SetLensValue((String)"lib_tripod_key"));
        libPatcher.setValueHex(_ShotParams_1downsample_1by_12_1before_1merge_1set, Helper.SetLensValue((String)"lib_downsamplebybeforemerge_key"));
        libPatcher.setValueHex(_ShotParams_1allow_1temporal_1binning_1set, Helper.SetLensValue((String)"lib_allowtemporalbinning_key"));
        libPatcher.setValueHex(_ShotParams_1allow_1base_1frame_1reuse_1set, Helper.SetLensValue((String)"lib_allowbaseframereuse_key"));
        libPatcher.setValueHex(_InitParams_1simultaneous_1merge_1and_1finish_1set, Helper.SetLensValue((String)"lib_simultaneousmerge_key"));
        libPatcher.setValueHex(_NoiseReductSabre1, Helper.SetLensValue((String)"lib_noisereductsabre1_key"));
        libPatcher.setValueHex(_SabreNoiseEstimals, Helper.SetLensValue((String)"lib_sabrenoiseestimals_key"));
        libPatcher.setValueHex(_HDRRatio3, Helper.SetLensValue((String)"lib_hdrratio3_key"));
        libPatcher.setValueHex(_Contrast4, Helper.SetLensValue((String)"lib_contrast4_key"));
        libPatcher.setValueHex(_Contrast5, Helper.SetLensValue((String)"lib_contrast5_key"));
        libPatcher.setValueHex(_RecomputeWBOnBaseFrame, Helper.SetLensValue((String)"lib_wbbaseframe_key"));
        libPatcher.setValueHex(_LumaDenoise, Helper.SetLensValue((String)"lib_lumadenoise_key"));
        libPatcher.setValueHex(_BrightN, Helper.SetLensValue((String)"lib_brightn_key"));
        libPatcher.setValueHex(_Darker, Helper.SetLensValue((String)"lib_darker_key"));
        libPatcher.setValueHex(_LumaSmooth, Helper.SetLensValue((String)"lib_lumasmooth_key"));
        libPatcher.setValueHex(_NROpacity, Helper.SetLensValue((String)"lib_noisereductopacity_key"));
        libPatcher.setValueHex(_DenSmoothing1, Helper.SetLensValue((String)"lib_lumasmoothing_key"));
        libPatcher.setValueHex(_DenSmoothing2, Helper.SetLensValue((String)"lib_denoisesmoothing_key"));
        libPatcher.setValueHex(_DehazeBlack, Helper.SetLensValue((String)"lib_dehazedblack_key"));
        libPatcher.setValueHex(_NContrast1, Helper.SetLensValue((String)"lib_ncontrast1_key"));
        libPatcher.setValueHex(_LumaNoise1, Helper.SetLensValue((String)"lib_lumanoise1_key"));
        libPatcher.setValueHex(_LumaNew, Helper.SetLensValue((String)"lib_lumanew_key"));
        libPatcher.setValueHex(_HDRRaw2, Helper.SetLensValue((String)"lib_hdrraw2_key"));
        libPatcher.setValueHex(_HDRSabreCalcVal1, Helper.SetLensValue((String)"lib_hdrsabrecalcval1_key"));
        libPatcher.setValueHex(_HDRSabreCalcVal2, Helper.SetLensValue((String)"lib_hdrsabrecalcval2_key"));
        libPatcher.setValueHex(_Robustness, Helper.SetLensValue((String)"lib_robustness_key"));
        libPatcher.setValueHex(_NoiseModelUnblock, Helper.SetLensValue((String)"lib_noisemodelunblock_key"));
        libPatcher.setValueHex(_RawCompress, Helper.SetLensValue((String)"lib_raw_compress_key"));
        libPatcher.setValueHex(_NightModeGain, Helper.SetLensValue((String)"lib_night_mode_gain_key"));
        libPatcher.setValueHex(_HDRModel, Helper.SetLensValue((String)"lib_hdrmodel_key"));
        libPatcher.setValueHex(_BlurPreview, Helper.SetLensValue((String)"lib_blurpreview_key"));
        libPatcher.setValueHex(_FixRaw16Merge, Helper.SetLensValue((String)"lib_fixraw16merge_key"));
        libPatcher.setValueHex(_HardJPGQuality, Helper.SetLensValue((String)"lib_hardjpgquality_key"));
        libPatcher.setValueHex(_LutNoiseFix, Helper.SetLensValue((String)"lib_lutnoisefix_key"));
        libPatcher.setValueHex(_LightFix, Helper.SetLensValue((String)"lib_lightfix_key"));
        libPatcher.setValueHex(_LightFix2, Helper.SetLensValue((String)"lib_lightfix2_key"));
        libPatcher.setValueHex(_LightFix3, Helper.SetLensValue((String)"lib_lightfix3_key"));
        libPatcher.setValueHex(_SkipMetadataCheck, Helper.SetLensValue((String)"lib_skipmetadatacheck_key"));
        libPatcher.setValueHex(_ShastaForce, Helper.SetLensValue((String)"lib_shastaforce_key"));
        libPatcher.setValueHex(_ShastaFactor, Helper.SetLensValue((String)"lib_shastafactor_key"));
        libPatcher.setValueHex(_ResamplMethod, Helper.SetLensValue((String)"lib_resamplmethod_key"));
        libPatcher.setValueHex(_AppDiGainSet, Helper.SetLensValue((String)"lib_appdigainset_key"));
        libPatcher.setValueHex(_SharpnessA, Helper.SetLensValue((String)"lib_sharpnessa_key"));
        libPatcher.setValueHex(_DiscardFramesWithTetMismatch, Helper.SetLensValue((String)"lib_withtetmismatch_key"));
        libPatcher.setValueHex(_MaxRelativeTetFactor, Helper.SetLensValue((String)"lib_maxrelativetetfactor_key"));
        libPatcher.setValueHex(_SharpGain, Helper.SetLensValue((String)"lib_sharpgain_key"));
        libPatcher.setValueHex(_SharpGainMacro, Helper.SetLensValue((String)"lib_sharpgainmacro_key"));
        libPatcher.setValueHex(_SharpGainMicro, Helper.SetLensValue((String)"lib_sharpgainmicro_key"));
        libPatcher.setValueHex(_SharpnessB, Helper.SetLensValue((String)"lib_sharpnessb_key"));
        libPatcher.setValueHex(_Denoise, Helper.SetLensValue((String)"lib_denoise_key"));
        libPatcher.setValueHex(_SpatialA, Helper.SetLensValue((String)"lib_spatiala_key"));
        libPatcher.setValueHex(_SpatialB, Helper.SetLensValue((String)"lib_spatialb_key"));
        libPatcher.setValueHex(_ChromaA, Helper.SetLensValue((String)"lib_chromaa_key"));
        libPatcher.setValueHex(_ChromaB, Helper.SetLensValue((String)"lib_chromab_key"));
        libPatcher.setValueHex(_LumaA, Helper.SetLensValue((String)"lib_lumaa_key"));
        libPatcher.setValueHex(_LumaB, Helper.SetLensValue((String)"lib_lumab_key"));
        libPatcher.setValueHex(_TemporalA, Helper.SetLensValue((String)"lib_temporala_key"));
        libPatcher.setValueHex(_TemporalB, Helper.SetLensValue((String)"lib_temporalb_key"));
        libPatcher.setValueHex(_LumaNoise, Helper.SetLensValue((String)"lib_lumanoise_key"));
        libPatcher.setValueHex(_Saturation, Helper.SetLensValue((String)"lib_saturation_key"));
        libPatcher.setValueHex(_Saturation2, Helper.SetLensValue((String)"lib_saturation2_key"));
        libPatcher.setValueHex(_Saturation3, Helper.SetLensValue((String)"lib_saturation3_key"));
        libPatcher.setValueHex(_ISO, Helper.SetLensValue((String)"pref_lib_iso_option_available_key"));
        libPatcher.setValueHex(_SharpShastaMotion, Helper.SetLensValue((String)"lib_sharpshastamotion_key"));
        libPatcher.setValueHex(_Depth1, Helper.SetLensValue((String)"lib_depth1_key"));
        libPatcher.setValueHex(_Depth2, Helper.SetLensValue((String)"lib_depth2_key"));
        libPatcher.setValueHex(_SharpMini, Helper.SetLensValue((String)"lib_sharpmini_key"));
        libPatcher.setValueHex(_SharpMacro, Helper.SetLensValue((String)"lib_sharpmacro_key"));
        libPatcher.setValueHex(_SharpeningEdge, Helper.SetLensValue((String)"lib_sharpeningedge_key"));
        libPatcher.setValueHex(_SoftSharpA, Helper.SetLensValue((String)"lib_softsharpa_key"));
        libPatcher.setValueHex(_SoftSharpB, Helper.SetLensValue((String)"lib_softsharpb_key"));
        libPatcher.setValueHex(_SoftSharpC, Helper.SetLensValue((String)"lib_softsharpc_key"));
        libPatcher.setValueHex(_SharpnessNoiseModel, Helper.SetLensValue((String)"lib_sharpnessnoisemodel_key"));
        libPatcher.setValueHex(_RaisrZFTuning1, Helper.SetLensValue((String)"lib_raisrzftuning1_key"));
        libPatcher.setValueHex(_RaisrZFTuning2, Helper.SetLensValue((String)"lib_raisrzftuning2_key"));
        libPatcher.setValueHex(_Zipper1, Helper.SetLensValue((String)"lib_zipper1_key"));
        libPatcher.setValueHex(_Zipper2, Helper.SetLensValue((String)"lib_zipper2_key"));
        libPatcher.setValueHex(_Zipper3, Helper.SetLensValue((String)"lib_zipper3_key"));
        libPatcher.setValueHex(_SabreSharp, Helper.SetLensValue((String)"lib_sabresharp_key"));
        libPatcher.setValueHex(_SabreSharp, Helper.SetLensValue((String)"lib_sabresharp_key"));
        libPatcher.setValueHex(_SabreSharp2, Helper.SetLensValue((String)"lib_sabresharp2_key"));
        libPatcher.setValueHex(_SabreSharp3, Helper.SetLensValue((String)"lib_sabresharp3_key"));
        libPatcher.setValueHex(_SabreContrastSharp, Helper.SetLensValue((String)"lib_sabrecontrastsharp_key"));
        libPatcher.setValueHex(_Exposition, Helper.SetLensValue((String)"lib_exposition_key"));
        libPatcher.setValueHex(_Exposure, Helper.SetLensValue((String)"lib_exposure_key"));
        libPatcher.setValueHex(_Darkenlight, Helper.SetLensValue((String)"lib_darkenlight_key"));
        libPatcher.setValueHex(_ExpoComp, Helper.SetLensValue((String)"lib_expocomp_key"));
        libPatcher.setValueHex(_ExpoCor, Helper.SetLensValue((String)"lib_expocor_key"));
        libPatcher.setValueHex(_IsoExpoTun, Helper.SetLensValue((String)"lib_isoexpotun_key"));
        libPatcher.setValueHex(_ExposureDarker, Helper.SetLensValue((String)"lib_exposure_darker_key"));
        libPatcher.setValueHex(_ExposureDarker2, Helper.SetLensValue((String)"lib_exposure_darker2_key"));
        libPatcher.setValueHex(_HardMerge, Helper.SetLensValue((String)"lib_hardmerge_key"));
        libPatcher.setValueHex(_SABRE1, Helper.SetLensValue((String)"lib_sabre1_key"));
        libPatcher.setValueHex(_SABRE2, Helper.SetLensValue((String)"lib_sabre2_key"));
        libPatcher.setValueHex(_SABRE3, Helper.SetLensValue((String)"lib_sabre3_key"));
        libPatcher.setValueHex(_CoefSabrTuNoise, Helper.SetLensValue((String)"lib_coefsabrtunoise_key"));
        libPatcher.setValueHex(_SabrBurMerge1, Helper.SetLensValue((String)"lib_sabrburmerge1_key"));
        libPatcher.setValueHex(_SabrBurMerge2, Helper.SetLensValue((String)"lib_sabrburmerge2_key"));
        libPatcher.setValueHex(_SabrBurMerge3, Helper.SetLensValue((String)"lib_sabrburmerge3_key"));
        libPatcher.setValueHex(_SmoothingSabre, Helper.SetLensValue((String)"lib_smoothingsabre_key"));
        libPatcher.setValueHex(_NoiseReductSabre, Helper.SetLensValue((String)"lib_noisereductsabre_key"));
        libPatcher.setValueHex(_SabreNoiseArt, Helper.SetLensValue((String)"lib_sabrenoiseart_key"));
        libPatcher.setValueHex(_BetterColWiener, Helper.SetLensValue((String)"lib_bettercolwiener_key"));
        libPatcher.setValueHex(_SavMergChrDen, Helper.SetLensValue((String)"lib_savmergchrden_key"));
        libPatcher.setValueHex(_FixNoiseSabre, Helper.SetLensValue((String)"lib_fixnoisesabre_key"));
        libPatcher.setValueHex(_ColProcessing, Helper.SetLensValue((String)"lib_colprocessing_key"));
        libPatcher.setValueHex(_FixShastaMerge, Helper.SetLensValue((String)"lib_fixshastamerge_key"));
        libPatcher.setValueHex(_VolumeProcessing1, Helper.SetLensValue((String)"lib_volumeprocessing1_key"));
        libPatcher.setValueHex(_VolumeProcessing2, Helper.SetLensValue((String)"lib_volumeprocessing2_key"));
        libPatcher.setValueHex(_Hotpixelsuppres, Helper.SetLensValue((String)"lib_hotpixelsuppres_key"));
        libPatcher.setValueHex(_SensorID, Helper.SetLensValue((String)"lib_sensorid_key"));
        libPatcher.setValueHex(_Smoothness, Helper.SetLensValue((String)"lib_smoothness_key"));
        libPatcher.setValueHex(_SabreByRAWToYUV, Helper.SetLensValue((String)"lib_sabrebyrawtoyuv_key"));
        libPatcher.setValueHex(_Smoothing1, Helper.SetLensValue((String)"lib_smoothing1_key"));
        libPatcher.setValueHex(_Smoothing2, Helper.SetLensValue((String)"lib_smoothing2_key"));
        libPatcher.setValueHex(_SmoothingNew, Helper.SetLensValue((String)"lib_smoothingnew_key"));
        libPatcher.setValueHex(_Brightnessintensity, Helper.SetLensValue((String)"lib_brightnessintensity_key"));
        libPatcher.setValueHex(_HDRBrightness, Helper.SetLensValue((String)"lib_hdrbrightness_key"));
        libPatcher.setValueHex(_HDR2, Helper.SetLensValue((String)"lib_hdr2_key"));
        libPatcher.setValueHex(_Hightlight2, Helper.SetLensValue((String)"lib_highlight2_key"));
        libPatcher.setValueHex(_HDRRatio2, Helper.SetLensValue((String)"lib_hdrratio2_key"));
        libPatcher.setValueHex(_AVGLDR, Helper.SetLensValue((String)"lib_avgldr_key"));
        libPatcher.setValueHex(_CContrast, Helper.SetLensValue((String)"lib_ccontrast_key"));
        libPatcher.setValueHex(_CContrast2, Helper.SetLensValue((String)"lib_ccontrast2_key"));
        libPatcher.setValueHex(_Dehazedregulator2, Helper.SetLensValue((String)"lib_dehazedregulator2_key"));
        libPatcher.setValueHex(_TemporalBinning, Helper.SetLensValue((String)"lib_temporalbin_key"));
        libPatcher.setValueHex(_TemporalRadius, Helper.SetLensValue((String)"lib_temporal_radius_key"));
        libPatcher.setValueHex(_ShotNoiseFactor, Helper.SetLensValue((String)"lib_shotnoisefactor_key"));
        libPatcher.setValueHex(_TunColSatPar1, Helper.SetLensValue((String)"lib_tuncolsatpar1_key"));
        libPatcher.setValueHex(_TunColSatPar2, Helper.SetLensValue((String)"lib_tuncolsatpar2_key"));
        libPatcher.setValueHex(_CG2, Helper.SetLensValue((String)"lib_cg2_key"));
        libPatcher.setValueHex(_CG3, Helper.SetLensValue((String)"lib_cg3_key"));
        libPatcher.setValueHex(_CG4, Helper.SetLensValue((String)"lib_cg4_key"));
        libPatcher.setValueHex(_CG5, Helper.SetLensValue((String)"lib_cg5_key"));
        libPatcher.setValueHex(_CG6, Helper.SetLensValue((String)"lib_cg6_key"));
        libPatcher.setValueHex(_CG9, Helper.SetLensValue((String)"lib_cg9_key"));
        libPatcher.setValueHex(_CG10, Helper.SetLensValue((String)"lib_cg10_key"));
        libPatcher.setValueHex(_Green, Helper.SetLensValue((String)"lib_green_key"));
        libPatcher.setValueHex(_Red, Helper.SetLensValue((String)"lib_red_key"));
        libPatcher.setValueHex(_BY, Helper.SetLensValue((String)"lib_by_key"));
        libPatcher.setValueHex(_YBP, Helper.SetLensValue((String)"lib_ybp_key"));
        libPatcher.setValueHex(_GRO, Helper.SetLensValue((String)"lib_gro_key"));
        libPatcher.setValueHex(_ORGB, Helper.SetLensValue((String)"lib_orgb_key"));
        libPatcher.setValueHex(_Vignette, Helper.SetLensValue((String)"lib_vignette_key"));
        libPatcher.setValueHex(_VignetteC, Helper.SetLensValue((String)"lib_vignettec_key"));
        libPatcher.setValueHex(_DehazedExpo, Helper.SetLensValue((String)"lib_dehazedexpo_key"));
        libPatcher.setValueHex(_Clarity, Helper.SetLensValue((String)"lib_clarity_key"));
        libPatcher.setValueHex(_ContrastL1, Helper.SetLensValue((String)"lib_contrast_1_key"));
        libPatcher.setValueHex(_ContrastL2, Helper.SetLensValue((String)"lib_contrast_2_key"));
        libPatcher.setValueHex(_Lighting, Helper.SetLensValue((String)"lib_lighting_key"));
        libPatcher.setValueHex(_HDRRangePlus, Helper.SetLensValue((String)"lib_hdrrangeplus_key"));
        libPatcher.setValueHex(_HDRRangeMinus, Helper.SetLensValue((String)"lib_hdrrangeminus_key"));
        libPatcher.setValueHex(_NightModeExposition, Helper.SetLensValue((String)"lib_nightmodeexposition_key"));
        libPatcher.setValueHex(_Light, Helper.SetLensValue((String)"lib_light_key"));
        libPatcher.setValueHex(_WhiteLevel, Helper.SetLensValue((String)"lib_whitelevel_key"));
        libPatcher.setValueHex(_HDROverLight, Helper.SetLensValue((String)"lib_hdroverlight_key"));
        libPatcher.setValueHex(_HDREffectInt, Helper.SetLensValue((String)"lib_hdreffectint_key"));
        libPatcher.setValueHex(_HDREffect, Helper.SetLensValue((String)"lib_hdreffect_key"));
        libPatcher.setValueHex(_SabreContrast, Helper.SetLensValue((String)"lib_sabrecontrast_key"));
        libPatcher.setValueHex(_ContrastBlack, Helper.SetLensValue((String)"lib_contrastblack_key"));
        libPatcher.setValueHex(_ShadowTuning, Helper.SetLensValue((String)"lib_shadowtuning_key"));
        libPatcher.setValueHex(_LumaDHSabreL1, Helper.SetLensValue((String)"lib_lumadhsabre_l1_key"));
        libPatcher.setValueHex(_LumaDHSabreL2, Helper.SetLensValue((String)"lib_lumadhsabre_l2_key"));
        libPatcher.setValueHex(_LumaDHSabreL3, Helper.SetLensValue((String)"lib_lumadhsabre_l3_key"));
        libPatcher.setValueHex(_LumaDHSabreL4, Helper.SetLensValue((String)"lib_lumadhsabre_l4_key"));
        libPatcher.setValueHex(_LumaDHSabreL5, Helper.SetLensValue((String)"lib_lumadhsabre_l5_key"));
        libPatcher.setValueHex(_LumaDLSabreL1, Helper.SetLensValue((String)"lib_lumadlsabre_l1_key"));
        libPatcher.setValueHex(_LumaDLSabreL2, Helper.SetLensValue((String)"lib_lumadlsabre_l2_key"));
        libPatcher.setValueHex(_LumaDLSabreL3, Helper.SetLensValue((String)"lib_lumadlsabre_l3_key"));
        libPatcher.setValueHex(_LumaDLSabreL4, Helper.SetLensValue((String)"lib_lumadlsabre_l4_key"));
        libPatcher.setValueHex(_LumaDLSabreL5, Helper.SetLensValue((String)"lib_lumadlsabre_l5_key"));
        libPatcher.setValueHex(_LumaDMSabreL1, Helper.SetLensValue((String)"lib_lumadmsabre_l1_key"));
        libPatcher.setValueHex(_LumaDMSabreL2, Helper.SetLensValue((String)"lib_lumadmsabre_l2_key"));
        libPatcher.setValueHex(_LumaDMSabreL3, Helper.SetLensValue((String)"lib_lumadmsabre_l3_key"));
        libPatcher.setValueHex(_LumaDMSabreL4, Helper.SetLensValue((String)"lib_lumadmsabre_l4_key"));
        libPatcher.setValueHex(_LumaDMSabreL5, Helper.SetLensValue((String)"lib_lumadmsabre_l5_key"));
        libPatcher.setValueHex(_SpatialDenMi1, Helper.SetLensValue((String)"lib_spatialdenmi1_key"));
        libPatcher.setValueHex(_SpatialDenMi2, Helper.SetLensValue((String)"lib_spatialdenmi2_key"));
        libPatcher.setValueHex(_SpatialDenMi3, Helper.SetLensValue((String)"lib_spatialdenmi3_key"));
        libPatcher.setValueHex(_SpatialDenMi4, Helper.SetLensValue((String)"lib_spatialdenmi4_key"));
        libPatcher.setValueHex(_LumaDHSabreL1A, Helper.SetLensValue((String)"lib_lumadhsabre_l1a_key"));
        libPatcher.setValueHex(_LumaDHSabreL1B, Helper.SetLensValue((String)"lib_lumadhsabre_l1b_key"));
        libPatcher.setValueHex(_LumaDHSabreL2A, Helper.SetLensValue((String)"lib_lumadhsabre_l2a_key"));
        libPatcher.setValueHex(_LumaDHSabreL2B, Helper.SetLensValue((String)"lib_lumadhsabre_l2b_key"));
        libPatcher.setValueHex(_LumaDHSabreL3A, Helper.SetLensValue((String)"lib_lumadhsabre_l3a_key"));
        libPatcher.setValueHex(_LumaDHSabreL3B, Helper.SetLensValue((String)"lib_lumadhsabre_l3b_key"));
        libPatcher.setValueHex(_LumaDHSabreL4A, Helper.SetLensValue((String)"lib_lumadhsabre_l4a_key"));
        libPatcher.setValueHex(_LumaDHSabreL4B, Helper.SetLensValue((String)"lib_lumadhsabre_l4b_key"));
        libPatcher.setValueHex(_LumaDHSabreL5A, Helper.SetLensValue((String)"lib_lumadhsabre_l5a_key"));
        libPatcher.setValueHex(_LumaDLSabreL1A, Helper.SetLensValue((String)"lib_lumadlsabre_l1a_key"));
        libPatcher.setValueHex(_LumaDLSabreL1B, Helper.SetLensValue((String)"lib_lumadlsabre_l1b_key"));
        libPatcher.setValueHex(_LumaDLSabreL2A, Helper.SetLensValue((String)"lib_lumadlsabre_l2a_key"));
        libPatcher.setValueHex(_LumaDLSabreL2B, Helper.SetLensValue((String)"lib_lumadlsabre_l2b_key"));
        libPatcher.setValueHex(_LumaDLSabreL3A, Helper.SetLensValue((String)"lib_lumadlsabre_l3a_key"));
        libPatcher.setValueHex(_LumaDLSabreL3B, Helper.SetLensValue((String)"lib_lumadlsabre_l3b_key"));
        libPatcher.setValueHex(_LumaDLSabreL4A, Helper.SetLensValue((String)"lib_lumadlsabre_l4a_key"));
        libPatcher.setValueHex(_LumaDLSabreL4B, Helper.SetLensValue((String)"lib_lumadlsabre_l4b_key"));
        libPatcher.setValueHex(_LumaDLSabreL5A, Helper.SetLensValue((String)"lib_lumadlsabre_l5a_key"));
        libPatcher.setValueHex(_LumaDMSabreL1A, Helper.SetLensValue((String)"lib_lumadmsabre_l1a_key"));
        libPatcher.setValueHex(_LumaDMSabreL1B, Helper.SetLensValue((String)"lib_lumadmsabre_l1b_key"));
        libPatcher.setValueHex(_LumaDMSabreL2A, Helper.SetLensValue((String)"lib_lumadmsabre_l2a_key"));
        libPatcher.setValueHex(_LumaDMSabreL2B, Helper.SetLensValue((String)"lib_lumadmsabre_l2b_key"));
        libPatcher.setValueHex(_LumaDMSabreL3A, Helper.SetLensValue((String)"lib_lumadmsabre_l3a_key"));
        libPatcher.setValueHex(_LumaDMSabreL3B, Helper.SetLensValue((String)"lib_lumadmsabre_l3b_key"));
        libPatcher.setValueHex(_LumaDMSabreL4A, Helper.SetLensValue((String)"lib_lumadmsabre_l4a_key"));
        libPatcher.setValueHex(_LumaDMSabreL4B, Helper.SetLensValue((String)"lib_lumadmsabre_l4b_key"));
        libPatcher.setValueHex(_LumaDMSabreL5A, Helper.SetLensValue((String)"lib_lumadmsabre_l5a_key"));
        libPatcher.setValueHex(_LumaDNewA, Helper.SetLensValue((String)"lib_lumadnewa_key"));
        libPatcher.setValueHex(_LumaDNewB, Helper.SetLensValue((String)"lib_lumadnewb_key"));
        libPatcher.setValueHex(_LumaDHL1, Helper.SetLensValue((String)"lib_lumadh_l1_key"));
        libPatcher.setValueHex(_LumaDHL2, Helper.SetLensValue((String)"lib_lumadh_l2_key"));
        libPatcher.setValueHex(_LumaDHL3, Helper.SetLensValue((String)"lib_lumadh_l3_key"));
        libPatcher.setValueHex(_LumaDHL4, Helper.SetLensValue((String)"lib_lumadh_l4_key"));
        libPatcher.setValueHex(_LumaDHL5, Helper.SetLensValue((String)"lib_lumadh_l5_key"));
        libPatcher.setValueHex(_LumaDLL1, Helper.SetLensValue((String)"lib_lumadl_l1_key"));
        libPatcher.setValueHex(_LumaDLL2, Helper.SetLensValue((String)"lib_lumadl_l2_key"));
        libPatcher.setValueHex(_LumaDLL3, Helper.SetLensValue((String)"lib_lumadl_l3_key"));
        libPatcher.setValueHex(_LumaDLL4, Helper.SetLensValue((String)"lib_lumadl_l4_key"));
        libPatcher.setValueHex(_LumaDLL5, Helper.SetLensValue((String)"lib_lumadl_l5_key"));
        libPatcher.setValueHex(_LumaDML1, Helper.SetLensValue((String)"lib_lumadm_l1_key"));
        libPatcher.setValueHex(_LumaDML2, Helper.SetLensValue((String)"lib_lumadm_l2_key"));
        libPatcher.setValueHex(_LumaDML3, Helper.SetLensValue((String)"lib_lumadm_l3_key"));
        libPatcher.setValueHex(_LumaDML4, Helper.SetLensValue((String)"lib_lumadm_l4_key"));
        libPatcher.setValueHex(_LumaDML5, Helper.SetLensValue((String)"lib_lumadm_l5_key"));
        libPatcher.setValueHex(_LumaDHSL1, Helper.SetLensValue((String)"lib_lumadhs_l1_key"));
        libPatcher.setValueHex(_LumaDHSL2, Helper.SetLensValue((String)"lib_lumadhs_l2_key"));
        libPatcher.setValueHex(_LumaDHSL3, Helper.SetLensValue((String)"lib_lumadhs_l3_key"));
        libPatcher.setValueHex(_LumaDHSL4, Helper.SetLensValue((String)"lib_lumadhs_l4_key"));
        libPatcher.setValueHex(_LumaDHSL5, Helper.SetLensValue((String)"lib_lumadhs_l5_key"));
        libPatcher.setValueHex(_LumaDLSL1, Helper.SetLensValue((String)"lib_lumadls_l1_key"));
        libPatcher.setValueHex(_LumaDLSL2, Helper.SetLensValue((String)"lib_lumadls_l2_key"));
        libPatcher.setValueHex(_LumaDLSL3, Helper.SetLensValue((String)"lib_lumadls_l3_key"));
        libPatcher.setValueHex(_LumaDLSL4, Helper.SetLensValue((String)"lib_lumadls_l4_key"));
        libPatcher.setValueHex(_LumaDLSL5, Helper.SetLensValue((String)"lib_lumadls_l5_key"));
        libPatcher.setValueHex(_LumaDMSL1, Helper.SetLensValue((String)"lib_lumadms_l1_key"));
        libPatcher.setValueHex(_LumaDMSL2, Helper.SetLensValue((String)"lib_lumadms_l2_key"));
        libPatcher.setValueHex(_LumaDMSL3, Helper.SetLensValue((String)"lib_lumadms_l3_key"));
        libPatcher.setValueHex(_LumaDMSL4, Helper.SetLensValue((String)"lib_lumadms_l4_key"));
        libPatcher.setValueHex(_LumaDMSL5, Helper.SetLensValue((String)"lib_lumadms_l5_key"));
        libPatcher.setValueHex(_SabreLNewL1, Helper.SetLensValue((String)"lib_sabrelnew_l1_key"));
        libPatcher.setValueHex(_SabreLNewL2, Helper.SetLensValue((String)"lib_sabrelnew_l2_key"));
        libPatcher.setValueHex(_SabreLNewL3, Helper.SetLensValue((String)"lib_sabrelnew_l3_key"));
        libPatcher.setValueHex(_SabreLNewL4, Helper.SetLensValue((String)"lib_sabrelnew_l4_key"));
        libPatcher.setValueHex(_SabreLNewL5, Helper.SetLensValue((String)"lib_sabrelnew_l5_key"));
        libPatcher.setValueHex(_SabreLNewNL1, Helper.SetLensValue((String)"lib_sabrelnewn_l1_key"));
        libPatcher.setValueHex(_SabreLNewNL2, Helper.SetLensValue((String)"lib_sabrelnewn_l2_key"));
        libPatcher.setValueHex(_SabreLNewNL3, Helper.SetLensValue((String)"lib_sabrelnewn_l3_key"));
        libPatcher.setValueHex(_SabreLNewNL4, Helper.SetLensValue((String)"lib_sabrelnewn_l4_key"));
        libPatcher.setValueHex(_SabreLNewNL5, Helper.SetLensValue((String)"lib_sabrelnewn_l5_key"));
        libPatcher.setValueHex(_SabreLNewNL6, Helper.SetLensValue((String)"lib_sabrelnewn_l6_key"));
        libPatcher.setValueHex(_SabreLNewNL7, Helper.SetLensValue((String)"lib_sabrelnewn_l7_key"));
        libPatcher.setValueHex(_SabreLNewNL8, Helper.SetLensValue((String)"lib_sabrelnewn_l8_key"));
        libPatcher.setValueHex(_SabreLNewNL9, Helper.SetLensValue((String)"lib_sabrelnewn_l9_key"));
        libPatcher.setValueHex(_WaveletLumaDenoiseSabreLevels, Helper.SetLensValue((String)"lib_lumalevel_preset_key"));
        libPatcher.setValueHex(_InitParams, Helper.SetLensValue((String)"lib_init_params_key"));
        libPatcher.setValueHex(_InitParams2, Helper.SetLensValue((String)"lib_init_params_key"));
        if (GetMenuValues.getIntValue((String)"lib_user_key_1") != 0) {
            libPatcher.setValueHex(GetMenuValues.getHexIntValue((String)"lib_user_addr_1"), "lib_user_value_1");
        }
        if (GetMenuValues.getIntValue((String)"lib_user_key_2") != 0) {
            libPatcher.setValueHex(GetMenuValues.getHexIntValue((String)"lib_user_addr_2"), "lib_user_value_2");
        }
        if (GetMenuValues.getIntValue((String)"lib_user_key_3") != 0) {
            libPatcher.setValueHex(GetMenuValues.getHexIntValue((String)"lib_user_addr_3"), "lib_user_value_3");
        }
        if (GetMenuValues.getIntValue((String)"lib_user_key_4") != 0) {
            libPatcher.setValueHex(GetMenuValues.getHexIntValue((String)"lib_user_addr_4"), "lib_user_value_4");
        }
        if (GetMenuValues.getIntValue((String)"lib_user_key_5") != 0) {
            libPatcher.setValueHex(GetMenuValues.getHexIntValue((String)"lib_user_addr_5"), "lib_user_value_5");
        }
        if (GetMenuValues.getIntValue((String)"lib_user_key_6") != 0) {
            libPatcher.setValueHex(GetMenuValues.getHexIntValue((String)"lib_user_addr_6"), "lib_user_value_6");
        }
        if (GetMenuValues.getIntValue((String)"lib_user_key_7") != 0) {
            libPatcher.setValueHex(GetMenuValues.getHexIntValue((String)"lib_user_addr_7"), "lib_user_value_7");
        }
        if (GetMenuValues.getIntValue((String)"lib_user_key_8") != 0) {
            libPatcher.setValueHex(GetMenuValues.getHexIntValue((String)"lib_user_addr_8"), "lib_user_value_8");
        }
        if (GetMenuValues.getIntValue((String)"lib_user_key_9") != 0) {
            libPatcher.setValueHex(GetMenuValues.getHexIntValue((String)"lib_user_addr_9"), "lib_user_value_9");
        }
        if (GetMenuValues.getIntValue((String)"lib_user_key_10") != 0) {
            libPatcher.setValueHex(GetMenuValues.getHexIntValue((String)"lib_user_addr_10"), "lib_user_value_10");
        }
        if (Helper.MenuValue((String)"pref_enable_ldr_key") != 0) {
            libPatcher.setValueHex(_LDR, "lib_ldr_key");
            libPatcher.setValueHex(_StartGamma, "lib_gamma_ldr_key");
            libPatcher.setValueHex(_StartTone, "lib_tone_ldr_key");
            libPatcher.setValueHex(_BrightN, "lib_brightn_ldr_key");
            libPatcher.setValueHex(_CContrast2, "lib_ccontrast_ldr_key");
            libPatcher.setValueHex(_AVGLDR, "lib_avgldr_ldr_key");
            libPatcher.setValueHex(_HDRRatio2, "lib_hdrratio2_ldr_key");
            libPatcher.setValueHex(_DehazeBlack, "lib_dehazedblack_ldr_key");
            libPatcher.setValueHex(_NContrast1, "lib_ncontrast1_ldr_key");
            libPatcher.setValueHex(_HDRRaw2, "lib_hdrraw2_ldr_key");
            libPatcher.setValueHex(_ContrastL1, "lib_contrast_1_ldr_key");
            libPatcher.setValueHex(_ContrastL2, "lib_contrast_2_ldr_key");
            libPatcher.setValueHex(_DehazedExpo, "lib_dehazedexpo_ldr_key");
            libPatcher.setValueHex(_HDREffect, "lib_hdreffect_ldr_key");
            libPatcher.setValueHex(_HDREffectInt, "lib_hdreffectint_ldr_key");
            libPatcher.setValueHex(_HDROverLight, "lib_hdroverlight_ldr_key");
            libPatcher.setValueHex(_HDRRangeMinus, "lib_hdrrangeminus_ldr_key");
            libPatcher.setValueHex(_HDRRangePlus, "lib_hdrrangeplus_ldr_key");
            libPatcher.setValueHex(_Light, "lib_light_ldr_key");
            libPatcher.setValueHex(_ContrastBlack, "lib_contrastblack_ldr_key");
            libPatcher.setValueHex(_SabreContrast, "lib_sabrecontrast_ldr_key");
            libPatcher.setValueHex(_Clarity, "lib_clarity_ldr_key");
            libPatcher.setValueHex(_ISO, "pref_lib_iso_option_available_ldr_key");
            libPatcher.setValueHex(_Brightnessintensity, "lib_brightnessintensity_ldr_key");
            libPatcher.setValueHex(_ShadowTuning, "lib_shadowtuning_ldr_key");
            libPatcher.setValueHex(_ShadowCompensation, "lib_shadow_compensation_ldr_key");
            libPatcher.setValueHex(_Saturation, "lib_saturation_ldr_key");
            libPatcher.setValueHex(_Saturation2, "lib_saturation2_ldr_key");
            libPatcher.setValueHex(_Saturation3, "lib_saturation3_ldr_key");
            libPatcher.setValueHex(_Exposure, "lib_exposure_ldr_key");
            libPatcher.setValueHex(_Exposition, "lib_exposition_ldr_key");
            libPatcher.setValueHex(_Hightlight2, "lib_highlight2_ldr_key");
            libPatcher.setValueHex(_HDRRatio3, "lib_hdrratio3_ldr_key");
        }
        if (Helper.MenuValue((String)"pref_enable_pro_key") != 0) {
            libPatcher.setValueHex(_NoiseReductSabre1, "lib_noisereductsabre1_pro_key");
            libPatcher.setValueHex(_SabreNoiseEstimals, "lib_sabrenoiseestimals_pro_key");
            libPatcher.setValueHex(_HDRRatio3, "lib_hdrratio3_pro_key");
            libPatcher.setValueHex(_Contrast4, "lib_contrast4_pro_key");
            libPatcher.setValueHex(_Contrast5, "lib_contrast5_pro_key");
            libPatcher.setValueHex(_Darker, "lib_darker_pro_key");
            libPatcher.setValueHex(_LumaDenoise, "lib_lumadenoise_pro_key");
            libPatcher.setValueHex(_LumaSmooth, "lib_lumasmooth_pro_key");
            libPatcher.setValueHex(_NROpacity, "lib_noisereductopacity_pro_key");
            libPatcher.setValueHex(_DenSmoothing1, "lib_lumasmoothing_pro_key");
            libPatcher.setValueHex(_DenSmoothing2, "lib_denoisesmoothing_pro_key");
            libPatcher.setValueHex(_DehazeBlack, "lib_dehazedblack_pro_key");
            libPatcher.setValueHex(_NContrast1, "lib_ncontrast1_pro_key");
            libPatcher.setValueHex(_LumaNoise1, "lib_lumanoise1_pro_key");
            libPatcher.setValueHex(_LumaNew, "lib_lumanew_pro_key");
            libPatcher.setValueHex(_HDRRaw2, "lib_hdrraw2_pro_key");
            libPatcher.setValueHex(_HDRSabreCalcVal1, "lib_hdrsabrecalcval1_pro_key");
            libPatcher.setValueHex(_HDRSabreCalcVal2, "lib_hdrsabrecalcval2_pro_key");
            libPatcher.setValueHex(_Robustness, "lib_robustness_pro_key");
            libPatcher.setValueHex(_ShadowCompensation, "lib_shadow_compensation_pro_key");
            libPatcher.setValueHex(_NightModeGain, "lib_night_mode_gain_pro_key");
            libPatcher.setValueHex(_InitParams, "lib_init_params_pro_key");
            libPatcher.setValueHex(_InitParams2, "lib_init_params_pro_key");
            libPatcher.setValueHex(_RawCompress, "lib_raw_compress_pro_key");
            libPatcher.setValueHex(_HDRModel, "lib_hdrmodel_pro_key");
            libPatcher.setValueHex(_BlurPreview, "lib_blurpreview_pro_key");
            libPatcher.setValueHex(_FixRaw16Merge, "lib_fixraw16merge_pro_key");
            libPatcher.setValueHex(_HardJPGQuality, "lib_hardjpgquality_pro_key");
            libPatcher.setValueHex(_LutNoiseFix, "lib_lutnoisefix_pro_key");
            libPatcher.setValueHex(_LightFix, "lib_lightfix_pro_key");
            libPatcher.setValueHex(_LightFix2, "lib_lightfix2_pro_key");
            libPatcher.setValueHex(_LightFix3, "lib_lightfix3_pro_key");
            libPatcher.setValueHex(_SkipMetadataCheck, "lib_skipmetadatacheck_pro_key");
            libPatcher.setValueHex(_ShastaForce, "lib_shastaforce_pro_key");
            libPatcher.setValueHex(_ShastaFactor, "lib_shastafactor_pro_key");
            libPatcher.setValueHex(_ResamplMethod, "lib_resamplmethod_pro_key");
            libPatcher.setValueHex(_AppDiGainSet, "lib_appdigainset_pro_key");
            libPatcher.setValueHex(_SharpnessA, "lib_sharpnessa_pro_key");
            libPatcher.setValueHex(_SharpnessB, "lib_sharpnessb_pro_key");
            libPatcher.setValueHex(_Denoise, "lib_denoise_pro_key");
            libPatcher.setValueHex(_SpatialA, "lib_spatiala_pro_key");
            libPatcher.setValueHex(_SpatialB, "lib_spatialb_pro_key");
            libPatcher.setValueHex(_ChromaA, "lib_chromaa_pro_key");
            libPatcher.setValueHex(_NightModeExposition, "lib_nightmodeexposition_pro_key");
            libPatcher.setValueHex(_BrightN, "lib_brightn_pro_key");
            libPatcher.setValueHex(_ChromaB, "lib_chromab_pro_key");
            libPatcher.setValueHex(_LumaA, "lib_lumaa_pro_key");
            libPatcher.setValueHex(_LumaB, "lib_lumab_pro_key");
            libPatcher.setValueHex(_SensorID, "lib_sensorid_pro_key");
            libPatcher.setValueHex(_TemporalA, "lib_temporala_pro_key");
            libPatcher.setValueHex(_TemporalB, "lib_temporalb_pro_key");
            libPatcher.setValueHex(_LumaNoise, "lib_lumanoise_pro_key");
            libPatcher.setValueHex(_Saturation, "lib_saturation_pro_key");
            libPatcher.setValueHex(_Saturation2, "lib_saturation2_pro_key");
            libPatcher.setValueHex(_Saturation3, "lib_saturation3_pro_key");
            libPatcher.setValueHex(_ISO, "pref_lib_iso_option_available_pro_key");
            libPatcher.setValueHex(_SharpShastaMotion, "lib_sharpshastamotion_pro_key");
            libPatcher.setValueHex(_HdrPlusInterface, "lib_hdrplusinterface_pro_key");
            libPatcher.setValueHex(_Depth1, "lib_depth1_pro_key");
            libPatcher.setValueHex(_Depth2, "lib_depth2_pro_key");
            libPatcher.setValueHex(_SharpMini, "lib_sharpmini_pro_key");
            libPatcher.setValueHex(_SharpMacro, "lib_sharpmacro_pro_key");
            libPatcher.setValueHex(_SharpeningEdge, "lib_sharpeningedge_pro_key");
            libPatcher.setValueHex(_SoftSharpA, "lib_softsharpa_pro_key");
            libPatcher.setValueHex(_SoftSharpB, "lib_softsharpb_pro_key");
            libPatcher.setValueHex(_SoftSharpC, "lib_softsharpc_pro_key");
            libPatcher.setValueHex(_SharpnessNoiseModel, "lib_sharpnessnoisemodel_pro_key");
            libPatcher.setValueHex(_SharpDRad1, "lib_sharpdrad1_pro_key");
            libPatcher.setValueHex(_SharpDRad2, "lib_sharpdrad1_pro_key");
            libPatcher.setValueHex(_RaisrZFTuning1, "lib_raisrzftuning1_pro_key");
            libPatcher.setValueHex(_RaisrZFTuning2, "lib_raisrzftuning2_pro_key");
            libPatcher.setValueHex(_Zipper1, "lib_zipper1_pro_key");
            libPatcher.setValueHex(_Zipper2, "lib_zipper2_pro_key");
            libPatcher.setValueHex(_Zipper3, "lib_zipper3_pro_key");
            libPatcher.setValueHex(_SabreSharp, "lib_sabresharp_pro_key");
            libPatcher.setValueHex(_SabreSharp, "lib_sabresharp_pro_key");
            libPatcher.setValueHex(_SabreSharp2, "lib_sabresharp2_pro_key");
            libPatcher.setValueHex(_SabreSharp3, "lib_sabresharp3_pro_key");
            libPatcher.setValueHex(_SabreContrastSharp, "lib_sabrecontrastsharp_pro_key");
            libPatcher.setValueHex(_Exposition, "lib_exposition_pro_key");
            libPatcher.setValueHex(_Exposure, "lib_exposure_pro_key");
            libPatcher.setValueHex(_Darkenlight, "lib_darkenlight_pro_key");
            libPatcher.setValueHex(_ExpoComp, "lib_expocomp_pro_key");
            libPatcher.setValueHex(_ExpoCor, "lib_expocor_pro_key");
            libPatcher.setValueHex(_IsoExpoTun, "lib_isoexpotun_pro_key");
            libPatcher.setValueHex(_ExposureDarker, "lib_exposure_darker_pro_key");
            libPatcher.setValueHex(_ExposureDarker2, "lib_exposure_darker2_pro_key");
            libPatcher.setValueHex(_HardMerge, "lib_hardmerge_pro_key");
            libPatcher.setValueHex(_SABRE1, "lib_sabre1_pro_key");
            libPatcher.setValueHex(_SABRE2, "lib_sabre2_pro_key");
            libPatcher.setValueHex(_SABRE3, "lib_sabre3_pro_key");
            libPatcher.setValueHex(_SabreByRAWToYUV, "lib_sabrebyrawtoyuv_pro_key");
            libPatcher.setValueHex(_Brightnessintensity, "lib_brightnessintensity_pro_key");
            libPatcher.setValueHex(_HDRBrightness, "lib_hdrbrightness_pro_key");
            libPatcher.setValueHex(_HDR2, "lib_hdr2_pro_key");
            libPatcher.setValueHex(_Hightlight2, "lib_highlight2_pro_key");
            libPatcher.setValueHex(_HDRRatio2, "lib_hdrratio2_pro_key");
            libPatcher.setValueHex(_AVGLDR, "lib_avgldr_pro_key");
            libPatcher.setValueHex(_Dehazedregulator2, "lib_dehazedregulator2_pro_key");
            libPatcher.setValueHex(_CoefSabrTuNoise, "lib_coefsabrtunoise_pro_key");
            libPatcher.setValueHex(_SabrBurMerge1, "lib_sabrburmerge1_pro_key");
            libPatcher.setValueHex(_SabrBurMerge2, "lib_sabrburmerge2_pro_key");
            libPatcher.setValueHex(_SabrBurMerge3, "lib_sabrburmerge3_pro_key");
            libPatcher.setValueHex(_SmoothingSabre, "lib_smoothingsabre_pro_key");
            libPatcher.setValueHex(_NoiseReductSabre, "lib_noisereductsabre_pro_key");
            libPatcher.setValueHex(_SabreNoiseArt, "lib_sabrenoiseart_pro_key");
            libPatcher.setValueHex(_BetterColWiener, "lib_bettercolwiener_pro_key");
            libPatcher.setValueHex(_SavMergChrDen, "lib_savmergchrden_pro_key");
            libPatcher.setValueHex(_FixNoiseSabre, "lib_fixnoisesabre_pro_key");
            libPatcher.setValueHex(_ColProcessing, "lib_colprocessing_pro_key");
            libPatcher.setValueHex(_FixShastaMerge, "lib_fixshastamerge_pro_key");
            libPatcher.setValueHex(_VolumeProcessing1, "lib_volumeprocessing1_pro_key");
            libPatcher.setValueHex(_VolumeProcessing2, "lib_volumeprocessing2_pro_key");
            libPatcher.setValueHex(_Hotpixelsuppres, "lib_hotpixelsuppres_pro_key");
            libPatcher.setValueHex(_Smoothness, "lib_smoothness_pro_key");
            libPatcher.setValueHex(_Smoothing1, "lib_smoothing1_pro_key");
            libPatcher.setValueHex(_Smoothing2, "lib_smoothing2_pro_key");
            libPatcher.setValueHex(_SmoothingNew, "lib_smoothingnew_pro_key");
            libPatcher.setValueHex(_TemporalBinning, "lib_temporalbin_pro_key");
            libPatcher.setValueHex(_TemporalRadius, "lib_temporal_radius_pro_key");
            libPatcher.setValueHex(_ShotNoiseFactor, "lib_shotnoisefactor_pro_key");
            libPatcher.setValueHex(_NoiseModelShot, "lib_noisemodelshot_pro_key");
            libPatcher.setValueHex(_TunColSatPar1, "lib_tuncolsatpar1_pro_key");
            libPatcher.setValueHex(_TunColSatPar2, "lib_tuncolsatpar2_pro_key");
            libPatcher.setValueHex(_DiscardFramesWithTetMismatch, "lib_withtetmismatch_pro_key");
            libPatcher.setValueHex(_MaxRelativeTetFactor, "lib_maxrelativetetfactor_pro_key");
            libPatcher.setValueHex(_SharpGain, "lib_sharpgain_pro_key");
            libPatcher.setValueHex(_SharpGainMacro, "lib_sharpgainmacro_pro_key");
            libPatcher.setValueHex(_SharpGainMicro, "lib_sharpgainmicro_pro_key");
            libPatcher.setValueHex(_Contr, "lib_contr_pro_key");
            libPatcher.setValueHex(_Sat4, "lib_sat4_pro_key");
            libPatcher.setValueHex(_HightlightCompensation2, "lib_hightlight2_pro_key");
            libPatcher.setValueHex(_TunSupressHotPixel, "lib_tunsupresshotpixel_pro_key");
            libPatcher.setValueHex(_ShotParams_1device_1is_1on_1tripod_1set, "lib_tripod_pro_key");
            libPatcher.setValueHex(_ShotParams_1downsample_1by_12_1before_1merge_1set, "lib_downsamplebybeforemerge_pro_key");
            libPatcher.setValueHex(_ShotParams_1allow_1temporal_1binning_1set, "lib_allowtemporalbinning_pro_key");
            libPatcher.setValueHex(_ShotParams_1allow_1base_1frame_1reuse_1set, "lib_allowbaseframereuse_pro_key");
            libPatcher.setValueHex(_InitParams_1simultaneous_1merge_1and_1finish_1set, "lib_simultaneousmerge_pro_key");
            libPatcher.setValueHex(_CG2, "lib_cg2_pro_key");
            libPatcher.setValueHex(_CG3, "lib_cg3_pro_key");
            libPatcher.setValueHex(_CG4, "lib_cg4_pro_key");
            libPatcher.setValueHex(_CG5, "lib_cg5_pro_key");
            libPatcher.setValueHex(_CG6, "lib_cg6_pro_key");
            libPatcher.setValueHex(_CG9, "lib_cg9_pro_key");
            libPatcher.setValueHex(_CG10, "lib_cg10_pro_key");
            libPatcher.setValueHex(_Green, "lib_green_pro_key");
            libPatcher.setValueHex(_Red, "lib_red_pro_key");
            libPatcher.setValueHex(_BY, "lib_by_pro_key");
            libPatcher.setValueHex(_YBP, "lib_ybp_pro_key");
            libPatcher.setValueHex(_GRO, "lib_gro_pro_key");
            libPatcher.setValueHex(_ORGB, "lib_orgb_pro_key");
            libPatcher.setValueHex(_Vignette, "lib_vignette_pro_key");
            libPatcher.setValueHex(_VignetteC, "lib_vignettec_pro_key");
            libPatcher.setValueHex(_DehazedExpo, "lib_dehazedexpo_pro_key");
            libPatcher.setValueHex(_Clarity, "lib_clarity_pro_key");
            libPatcher.setValueHex(_ContrastL1, "lib_contrast_1_pro_key");
            libPatcher.setValueHex(_ContrastL2, "lib_contrast_2_pro_key");
            libPatcher.setValueHex(_ContrastL3a, "lib_contrast_3a_pro_key");
            libPatcher.setValueHex(_Lighting, "lib_lighting_pro_key");
            libPatcher.setValueHex(_HDRRangePlus, "lib_hdrrangeplus_pro_key");
            libPatcher.setValueHex(_HDRRangeMinus, "lib_hdrrangeminus_pro_key");
            libPatcher.setValueHex(_Light, "lib_light_pro_key");
            libPatcher.setValueHex(_BlackLevel, "lib_blacklevel_pro_key");
            libPatcher.setValueHex(_WhiteLevel, "lib_whitelevel_pro_key");
            libPatcher.setValueHex(_HDROverLight, "lib_hdroverlight_pro_key");
            libPatcher.setValueHex(_HDREffectInt, "lib_hdreffectint_pro_key");
            libPatcher.setValueHex(_HDREffect, "lib_hdreffect_pro_key");
            libPatcher.setValueHex(_SabreContrast, "lib_sabrecontrast_pro_key");
            libPatcher.setValueHex(_ContrastBlack, "lib_contrastblack_pro_key");
            libPatcher.setValueHex(_ShadowTuning, "lib_shadowtuning_pro_key");
            libPatcher.setValueHex(_SoftContrast, "lib_softcontrast_pro_key");
            libPatcher.setValueHex(_LumaDHSabreL1, "lib_lumadhsabre_l1_pro_key");
            libPatcher.setValueHex(_LumaDHSabreL2, "lib_lumadhsabre_l2_pro_key");
            libPatcher.setValueHex(_LumaDHSabreL3, "lib_lumadhsabre_l3_pro_key");
            libPatcher.setValueHex(_LumaDHSabreL4, "lib_lumadhsabre_l4_pro_key");
            libPatcher.setValueHex(_LumaDHSabreL5, "lib_lumadhsabre_l5_pro_key");
            libPatcher.setValueHex(_LumaDLSabreL1, "lib_lumadlsabre_l1_pro_key");
            libPatcher.setValueHex(_LumaDLSabreL2, "lib_lumadlsabre_l2_pro_key");
            libPatcher.setValueHex(_LumaDLSabreL3, "lib_lumadlsabre_l3_pro_key");
            libPatcher.setValueHex(_LumaDLSabreL4, "lib_lumadlsabre_l4_pro_key");
            libPatcher.setValueHex(_LumaDLSabreL5, "lib_lumadlsabre_l5_pro_key");
            libPatcher.setValueHex(_LumaDMSabreL1, "lib_lumadmsabre_l1_pro_key");
            libPatcher.setValueHex(_LumaDMSabreL2, "lib_lumadmsabre_l2_pro_key");
            libPatcher.setValueHex(_LumaDMSabreL3, "lib_lumadmsabre_l3_pro_key");
            libPatcher.setValueHex(_LumaDMSabreL4, "lib_lumadmsabre_l4_pro_key");
            libPatcher.setValueHex(_LumaDMSabreL5, "lib_lumadmsabre_l5_pro_key");
            libPatcher.setValueHex(_SpatialDenMi1, "lib_spatialdenmi1_pro_key");
            libPatcher.setValueHex(_SpatialDenMi2, "lib_spatialdenmi2_pro_key");
            libPatcher.setValueHex(_SpatialDenMi3, "lib_spatialdenmi3_pro_key");
            libPatcher.setValueHex(_SpatialDenMi4, "lib_spatialdenmi4_pro_key");
            libPatcher.setValueHex(_WaveletLumaDenoiseSabreLevels, "lib_lumalevel_preset_pro_key");
            libPatcher.setValueHex(_LumaDHSabreL1A, "lib_lumadhsabre_l1a_pro_key");
            libPatcher.setValueHex(_LumaDHSabreL1B, "lib_lumadhsabre_l1b_pro_key");
            libPatcher.setValueHex(_LumaDHSabreL2A, "lib_lumadhsabre_l2a_pro_key");
            libPatcher.setValueHex(_LumaDHSabreL2B, "lib_lumadhsabre_l2b_pro_key");
            libPatcher.setValueHex(_LumaDHSabreL3A, "lib_lumadhsabre_l3a_pro_key");
            libPatcher.setValueHex(_LumaDHSabreL3B, "lib_lumadhsabre_l3b_pro_key");
            libPatcher.setValueHex(_LumaDHSabreL4A, "lib_lumadhsabre_l4a_pro_key");
            libPatcher.setValueHex(_LumaDHSabreL4B, "lib_lumadhsabre_l4b_pro_key");
            libPatcher.setValueHex(_LumaDHSabreL5A, "lib_lumadhsabre_l5a_pro_key");
            libPatcher.setValueHex(_LumaDLSabreL1A, "lib_lumadlsabre_l1a_pro_key");
            libPatcher.setValueHex(_LumaDLSabreL1B, "lib_lumadlsabre_l1b_pro_key");
            libPatcher.setValueHex(_LumaDLSabreL2A, "lib_lumadlsabre_l2a_pro_key");
            libPatcher.setValueHex(_LumaDLSabreL2B, "lib_lumadlsabre_l2b_pro_key");
            libPatcher.setValueHex(_LumaDLSabreL3A, "lib_lumadlsabre_l3a_pro_key");
            libPatcher.setValueHex(_LumaDLSabreL3B, "lib_lumadlsabre_l3b_pro_key");
            libPatcher.setValueHex(_LumaDLSabreL4A, "lib_lumadlsabre_l4a_pro_key");
            libPatcher.setValueHex(_LumaDLSabreL4B, "lib_lumadlsabre_l4b_pro_key");
            libPatcher.setValueHex(_LumaDLSabreL5A, "lib_lumadlsabre_l5a_pro_key");
            libPatcher.setValueHex(_LumaDMSabreL1A, "lib_lumadmsabre_l1a_pro_key");
            libPatcher.setValueHex(_LumaDMSabreL1B, "lib_lumadmsabre_l1b_pro_key");
            libPatcher.setValueHex(_LumaDMSabreL2A, "lib_lumadmsabre_l2a_pro_key");
            libPatcher.setValueHex(_LumaDMSabreL2B, "lib_lumadmsabre_l2b_pro_key");
            libPatcher.setValueHex(_LumaDMSabreL3A, "lib_lumadmsabre_l3a_pro_key");
            libPatcher.setValueHex(_LumaDMSabreL3B, "lib_lumadmsabre_l3b_pro_key");
            libPatcher.setValueHex(_LumaDMSabreL4A, "lib_lumadmsabre_l4a_pro_key");
            libPatcher.setValueHex(_LumaDMSabreL4B, "lib_lumadmsabre_l4b_pro_key");
            libPatcher.setValueHex(_LumaDMSabreL5A, "lib_lumadmsabre_l5a_pro_key");
            libPatcher.setValueHex(_LumaDNewA, "lib_lumadnewa_pro_key");
            libPatcher.setValueHex(_LumaDNewB, "lib_lumadnewb_pro_key");
            libPatcher.setValueHex(_LumaDHL1, "lib_lumadh_l1_pro_key");
            libPatcher.setValueHex(_LumaDHL2, "lib_lumadh_l2_pro_key");
            libPatcher.setValueHex(_LumaDHL3, "lib_lumadh_l3_pro_key");
            libPatcher.setValueHex(_LumaDHL4, "lib_lumadh_l4_pro_key");
            libPatcher.setValueHex(_LumaDHL5, "lib_lumadh_l5_pro_key");
            libPatcher.setValueHex(_LumaDLL1, "lib_lumadl_l1_pro_key");
            libPatcher.setValueHex(_LumaDLL2, "lib_lumadl_l2_pro_key");
            libPatcher.setValueHex(_LumaDLL3, "lib_lumadl_l3_pro_key");
            libPatcher.setValueHex(_LumaDLL4, "lib_lumadl_l4_pro_key");
            libPatcher.setValueHex(_LumaDLL5, "lib_lumadl_l5_pro_key");
            libPatcher.setValueHex(_LumaDML1, "lib_lumadm_l1_pro_key");
            libPatcher.setValueHex(_LumaDML2, "lib_lumadm_l2_pro_key");
            libPatcher.setValueHex(_LumaDML3, "lib_lumadm_l3_pro_key");
            libPatcher.setValueHex(_LumaDML4, "lib_lumadm_l4_pro_key");
            libPatcher.setValueHex(_LumaDML5, "lib_lumadm_l5_pro_key");
            libPatcher.setValueHex(_LumaDHSL1, "lib_lumadhs_l1_pro_key");
            libPatcher.setValueHex(_LumaDHSL2, "lib_lumadhs_l2_pro_key");
            libPatcher.setValueHex(_LumaDHSL3, "lib_lumadhs_l3_pro_key");
            libPatcher.setValueHex(_LumaDHSL4, "lib_lumadhs_l4_pro_key");
            libPatcher.setValueHex(_LumaDHSL5, "lib_lumadhs_l5_pro_key");
            libPatcher.setValueHex(_LumaDLSL1, "lib_lumadls_l1_pro_key");
            libPatcher.setValueHex(_LumaDLSL2, "lib_lumadls_l2_pro_key");
            libPatcher.setValueHex(_LumaDLSL3, "lib_lumadls_l3_pro_key");
            libPatcher.setValueHex(_LumaDLSL4, "lib_lumadls_l4_pro_key");
            libPatcher.setValueHex(_LumaDLSL5, "lib_lumadls_l5_pro_key");
            libPatcher.setValueHex(_LumaDMSL1, "lib_lumadms_l1_pro_key");
            libPatcher.setValueHex(_LumaDMSL2, "lib_lumadms_l2_pro_key");
            libPatcher.setValueHex(_LumaDMSL3, "lib_lumadms_l3_pro_key");
            libPatcher.setValueHex(_LumaDMSL4, "lib_lumadms_l4_pro_key");
            libPatcher.setValueHex(_LumaDMSL5, "lib_lumadms_l5_pro_key");
            libPatcher.setValueHex(_SabreLNewL1, "lib_sabrelnew_l1_pro_key");
            libPatcher.setValueHex(_SabreLNewL2, "lib_sabrelnew_l2_pro_key");
            libPatcher.setValueHex(_SabreLNewL3, "lib_sabrelnew_l3_pro_key");
            libPatcher.setValueHex(_SabreLNewL4, "lib_sabrelnew_l4_pro_key");
            libPatcher.setValueHex(_SabreLNewL5, "lib_sabrelnew_l5_pro_key");
            libPatcher.setValueHex(_SabreLNewNL1, "lib_sabrelnewn_l1_pro_key");
            libPatcher.setValueHex(_SabreLNewNL2, "lib_sabrelnewn_l2_pro_key");
            libPatcher.setValueHex(_SabreLNewNL3, "lib_sabrelnewn_l3_pro_key");
            libPatcher.setValueHex(_SabreLNewNL4, "lib_sabrelnewn_l4_pro_key");
            libPatcher.setValueHex(_SabreLNewNL5, "lib_sabrelnewn_l5_pro_key");
            libPatcher.setValueHex(_SabreLNewNL6, "lib_sabrelnewn_l6_pro_key");
            libPatcher.setValueHex(_SabreLNewNL7, "lib_sabrelnewn_l7_pro_key");
            libPatcher.setValueHex(_SabreLNewNL8, "lib_sabrelnewn_l8_pro_key");
            libPatcher.setValueHex(_SabreLNewNL9, "lib_sabrelnewn_l9_pro_key");
            libPatcher.setValueHex(_CContrast, "lib_ccontrast_pro_key");
            libPatcher.setValueHex(_CContrast2, "lib_ccontrast2_pro_key");
            libPatcher.setValueHex(_RecomputeWBOnBaseFrame, "lib_wbbaseframe_pro_key");
        }
        Context context = libPatcher.getAppContext();
        boolean bl2 = bl = libPatcher.loadCustomLib(context);
        if (!bl) {
            Toast.makeText((Context)context, (CharSequence)"loadCustomLib ERROR", (int)1).show();
            bl2 = false;
        }
        return bl2;
    }

    private static boolean copyLibDisabled(LibPatcher libPatcher) {
        boolean bl;
        Context context = libPatcher.getAppContext();
        boolean bl2 = bl = libPatcher.loadCustomLib(context);
        if (!bl) {
            Toast.makeText((Context)context, (CharSequence)"loadCustomLib ERROR", (int)1).show();
            bl2 = false;
        }
        return bl2;
    }

    private static boolean copySignature(LibPatcher libPatcher) {
        String string = LibPatcher.getLibSignature();
        if (GetMenuValues.getIntValue((String)"pref_save_patchedlib_key") != 0 && GetMenuValues.getIntValue((String)"pref_sign_library_key") != 0) {
            Pref.setMenuValue((String)"info_libsignature_key", (String)string);
            libPatcher.setValueHex(_LibSignature, "info_libsignature_key");
        }
        return true;
    }

    private String doubleToHex(double d) {
        if (d == 0.0) {
            return "0000000000000000";
        }
        return this.reverseHex(String.format("%X", Double.doubleToLongBits(d)));
    }

    public static String getLibSignature() {
        Object object = Pref.getStringValue((String)"pref_signtext_key").trim();
        CharSequence charSequence = new StringBuilder();
        charSequence.append("");
        object = ((String)object).toCharArray();
        int n = ((Object)object).length;
        for (int i = 0; i < n; ++i) {
            charSequence.append(Integer.toHexString((int)object[i]));
        }
        charSequence = charSequence.toString().concat("0000000000000000000000000000000000000000000000000000000000000000").substring(0, 64);
        Pref.setMenuValue((String)"info_libsignature_key", (String)charSequence);
        return charSequence;
    }

    private byte[] hexStringToByteArray(String string) {
        int n = string.length();
        byte[] byArray = new byte[n / 2];
        for (int i = 0; i < n; i += 2) {
            byArray[i / 2] = (byte)((Character.digit(string.charAt(i), 16) << 4) + Character.digit(string.charAt(i + 1), 16));
        }
        return byArray;
    }

    /*
     * Enabled aggressive block sorting
     */
    public static void loadLibX(String string) {
        String string2;
        int n = Pref.MenuValue((String)"libs_key");
        if (n < 0) {
            string2 = Pref.getStringValue((String)"pref_libs_fromdir_key");
        } else {
            switch (n) {
                default: {
                    string2 = "libgcastartup.so";
                    break;
                }
                case 0: {
                    string2 = "libgcastartup.so";
                    break;
                }
                case 1: {
                    string2 = "libgcastartup_1.so";
                    break;
                }
                case 2: {
                    string2 = "libgcastartup_2.so";
                    break;
                }
                case 3: {
                    string2 = "libgcastartup_3.so";
                    break;
                }
                case 4: {
                    string2 = "libgcastartup_4.so";
                    break;
                }
                case 5: {
                    string2 = "libgcastartup_5.so";
                    break;
                }
                case 6: {
                    string2 = "libgcastartup_6.so";
                    break;
                }
                case 7: {
                    string2 = "libgcastartup_7.so";
                    break;
                }
                case 8: {
                    string2 = "libgcastartup_8.so";
                    break;
                }
                case 9: {
                    string2 = "libgcastartup_9.so";
                    break;
                }
                case 10: {
                    string2 = "libgcastartup_a.so";
                    break;
                }
                case 11: {
                    string2 = "libgcastartup_b.so";
                    break;
                }
                case 12: {
                    string2 = "libgcastartup_c.so";
                    break;
                }
                case 13: {
                    string2 = "libgcastartup_d.so";
                    break;
                }
                case 14: {
                    string2 = "libgcastartup_e.so";
                    break;
                }
                case 15: {
                    string2 = "libgcastartup_f.so";
                }
            }
        }
        if (GetMenuValues.getIntValue((String)"pref_enable_patcher_key") == 0) {
            if (LibPatcher.applyPatcherDisabled((String)string2)) return;
            System.loadLibrary(string);
            return;
        } else {
            if (LibPatcher.applyPatcher((String)string2)) return;
            System.loadLibrary(string);
        }
    }

    private String readBytes(long l, int n) {
        Context context = GetMenuValues.getAppContext();
        Object object = context.getFilesDir();
        if (object == null) {
            if (this.showToast) {
                Toast.makeText((Context)context, (CharSequence)"appContext.getFilesDir() == null", (int)1).show();
            }
            return "";
        }
        Object object2 = new File((File)object, this.libName);
        if (!((File)object2).exists()) {
            if (this.showToast) {
                Toast.makeText((Context)context, (CharSequence)"not patchedLib.exists()", (int)1).show();
            }
            return "";
        }
        object = new RandomAccessFile((File)object2, "r");
        object2 = new byte[n];
        try {
            ((RandomAccessFile)object).seek(l);
            ((RandomAccessFile)object).read((byte[])object2);
            ((RandomAccessFile)object).close();
        }
        catch (IOException iOException) {
            try {
                if (this.showToast) {
                    Toast.makeText((Context)context, (CharSequence)"readBytes: IOException", (int)1).show();
                }
                return "";
            }
            catch (FileNotFoundException fileNotFoundException) {
                if (this.showToast) {
                    Toast.makeText((Context)context, (CharSequence)"readBytes: FileNotFoundException", (int)1).show();
                }
                return "";
            }
        }
        object = this.bytesToHex((byte[])object2);
        if (this.showToast) {
            Toast.makeText((Context)context, (CharSequence)object, (int)1).show();
        }
        return object;
    }

    private String reverseHex(String string) {
        int n = string.length() / 2;
        char[] cArray = new char[n * 2];
        for (int i = 0; i < n; ++i) {
            int n2 = (n - 1 - i) * 2;
            int n3 = i * 2;
            cArray[n2] = string.charAt(n3);
            cArray[n2 + 1] = string.charAt(n3 + 1);
        }
        return new String(cArray);
    }

    private boolean streamToFile(InputStream inputStream, File object) throws IOException {
        int n;
        byte[] byArray = new byte[32256];
        object = new FileOutputStream((File)object, false);
        while ((n = inputStream.read(byArray)) > 0) {
            ((OutputStream)object).write(byArray, 0, n);
        }
        ((OutputStream)object).close();
        inputStream.close();
        return true;
    }

    private String writeBytes(long l, String object, Integer serializable) {
        if (((String)object).length() != ((Integer)serializable).intValue()) {
            serializable = new StringBuilder();
            ((StringBuilder)serializable).append((String)object);
            ((StringBuilder)serializable).append("HEX has wrong length");
            return ((StringBuilder)serializable).toString();
        }
        serializable = GetMenuValues.getAppContext().getFilesDir();
        if (serializable == null) {
            return "writeBytes: appContext.getFilesDir() == null";
        }
        if (!((File)(serializable = new File((File)serializable, this.libName))).exists()) {
            return "writeBytes: not patchedLib.exists()";
        }
        if (!((File)serializable).canWrite()) {
            return "writeBytes: readonly";
        }
        byte[] byArray = this.hexStringToByteArray((String)object);
        object = new RandomAccessFile((File)serializable, "rws");
        try {
            ((RandomAccessFile)object).seek(l);
            ((RandomAccessFile)object).write(byArray);
            ((RandomAccessFile)object).close();
            return "OK";
        }
        catch (IOException iOException) {
            try {
                serializable = new StringBuilder();
                ((StringBuilder)serializable).append("writeBytes: IOException: ");
                ((StringBuilder)serializable).append(iOException.toString());
                String string = ((StringBuilder)serializable).toString();
                return string;
            }
            catch (FileNotFoundException fileNotFoundException) {
                object = new StringBuilder();
                ((StringBuilder)object).append("writeBytes: FileNotFoundException: ");
                ((StringBuilder)object).append(fileNotFoundException.toString());
                return ((StringBuilder)object).toString();
            }
        }
    }

    public Context getAppContext() {
        Application application = AppGlobals.getInitialApplication();
        return application.createPackageContext(application.getPackageName(), 1).getApplicationContext();
    }

    public boolean loadCustomLib(Context context) {
        File file = context.getFilesDir();
        if (file == null) {
            return false;
        }
        if (!(file = new File(file, "libpatched_jni.so")).exists()) {
            return false;
        }
        Serializable serializable = new StringBuilder();
        ((StringBuilder)serializable).append(context.getApplicationInfo().nativeLibraryDir);
        ((StringBuilder)serializable).append(File.separator);
        ((StringBuilder)serializable).append("libgcastartup.so");
        serializable = new File(((StringBuilder)serializable).toString());
        if (file.length() != ((File)serializable).length()) {
            return false;
        }
        try {
            System.load(file.getAbsolutePath());
            return true;
        }
        catch (UnsatisfiedLinkError unsatisfiedLinkError) {
            Toast.makeText((Context)context, (CharSequence)unsatisfiedLinkError.toString(), (int)1).show();
            return false;
        }
        catch (Exception exception) {
            Toast.makeText((Context)context, (CharSequence)exception.toString(), (int)1).show();
            return false;
        }
    }

    public String moveLibToDir(String string) {
        Object object;
        int n = GetMenuValues.getIntValue((String)"libs_key");
        Object object2 = GetMenuValues.getAppContext();
        File file = object2.getFilesDir();
        if (file == null) {
            return "getFilesDir not found";
        }
        if ((file = new File(file, "libpatched_jni.so")).exists() && !file.delete()) {
            return "Error deleting patched lib";
        }
        if (n < 0) {
            object2 = Environment.getExternalStorageDirectory();
            object = new StringBuilder();
            ((StringBuilder)object).append("/LMC8.4/libs/");
            ((StringBuilder)object).append(string);
            string = ((StringBuilder)object).toString();
            object2 = new File((File)object2, string);
        } else {
            object2 = String.valueOf(object2.getApplicationInfo().nativeLibraryDir);
            object = new StringBuilder();
            ((StringBuilder)object).append("/");
            ((StringBuilder)object).append(string);
            string = ((String)object2).concat(((StringBuilder)object).toString());
            object2 = new File(string);
        }
        try {
            object = new FileInputStream((File)object2);
            BufferedInputStream bufferedInputStream = new BufferedInputStream((InputStream)object, 32256);
            string = !this.streamToFile((InputStream)bufferedInputStream, file) ? "streamToFile error" : "OK";
            return string;
        }
        catch (IOException iOException) {
            return "moveLibToDir: IOException";
        }
        catch (FileNotFoundException fileNotFoundException) {
            return String.valueOf("moveLibToDir: FileNotFoundException ").concat(string);
        }
    }

    public String moveLibToDir2(String string) {
        File file = GetMenuValues.getAppContext().getFilesDir();
        if (file == null) {
            return "getFilesDir not found";
        }
        file = new File(file, "libpatched_jni.so");
        File file2 = Environment.getExternalStorageDirectory();
        Object object = new StringBuilder();
        ((StringBuilder)object).append("/LMC8.4/patchedlibs/");
        ((StringBuilder)object).append("libpatched_jni.so");
        file2 = new File(file2, ((StringBuilder)object).toString());
        if (file2.exists() && !file2.delete()) {
            return "Error deleting patched lib";
        }
        try {
            FileInputStream fileInputStream = new FileInputStream(file);
            object = new BufferedInputStream(fileInputStream, 32256);
            string = !this.streamToFile((InputStream)object, file2) ? "streamToFile error" : "OK";
            return string;
        }
        catch (IOException iOException) {
            return "moveLibToDir: IOException";
        }
        catch (FileNotFoundException fileNotFoundException) {
            return String.valueOf("moveLibToDir: FileNotFoundException ").concat(string);
        }
    }

    public void setGammaCurve() {
        double[] dArray = getGammaCurve.getGammaCurve((int)-1);
        long l = _StartGamma;
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("");
        stringBuilder.append(gammaPresetName);
        stringBuilder.append("\n");
        stringBuilder.append("\n");
        for (int i = 0; i < 33; ++i) {
            double d = dArray[i];
            stringBuilder.append(Double.toString(d));
            stringBuilder.append("\n");
            this.writeBytes(l, this.doubleToHex(d), Integer.valueOf(16));
            l += 8L;
        }
        stringBuilder.toString();
    }

    public void setToneCurve() {
        double[] dArray = getToneCurve.getToneCurve((int)-1);
        long l = _StartTone;
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("");
        stringBuilder.append(tonePresetName);
        stringBuilder.append("\n");
        stringBuilder.append("\n");
        for (int i = 0; i < 17; ++i) {
            double d = dArray[i];
            stringBuilder.append(Double.toString(d));
            stringBuilder.append("\n");
            this.writeBytes(l, this.doubleToHex(d), Integer.valueOf(16));
            l += 8L;
        }
        stringBuilder.toString();
    }

    public void setValueHex(int n, String string) {
        int n2 = (string = GetMenuValues.getString((String)string)).length();
        if (n2 >= 2) {
            this.writeBytes((long)n, string, Integer.valueOf(n2));
        }
    }

    public void setValueHexToo(int n, String string) {
        int n2 = string.length();
        if (n2 >= 2) {
            this.writeBytes((long)n, string, Integer.valueOf(n2));
        }
    }
}

