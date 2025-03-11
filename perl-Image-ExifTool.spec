#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : perl-Image-ExifTool
Version  : 13.25
Release  : 18
URL      : https://exiftool.org/Image-ExifTool-13.25.tar.gz
Source0  : https://exiftool.org/Image-ExifTool-13.25.tar.gz
Summary  : perl module for image data extraction
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0-or-later
Requires: perl-Image-ExifTool-bin = %{version}-%{release}
Requires: perl-Image-ExifTool-man = %{version}-%{release}
Requires: perl-Image-ExifTool-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
ExifTool is a customizable set of Perl modules plus a full-featured
command-line application for reading and writing meta information in a wide
variety of files, including the maker note information of many digital
cameras by various manufacturers such as Canon, Casio, DJI, FLIR, FujiFilm,
GE, GoPro, HP, JVC/Victor, Kodak, Leaf, Minolta/Konica-Minolta, Nikon,
Nintendo, Olympus/Epson, Panasonic/Leica, Pentax/Asahi, Phase One, Reconyx,
Ricoh, Samsung, Sanyo, Sigma/Foveon and Sony.

Below is a list of file types and meta information formats currently
supported by ExifTool (r = read, w = write, c = create):

  File Types
  ------------+-------------+-------------+-------------+------------
  360   r/w   | DOCX  r     | ITC   r     | NUMBERS r   | RAM   r
  3FR   r     | DPX   r     | J2C   r     | NXD   r     | RAR   r
  3G2   r/w   | DR4   r/w/c | JNG   r/w   | O     r     | RAW   r/w
  3GP   r/w   | DSS   r     | JP2   r/w   | ODP   r     | RIFF  r
  7Z    r     | DV    r     | JPEG  r/w   | ODS   r     | RSRC  r
  A     r     | DVB   r/w   | JSON  r     | ODT   r     | RTF   r
  AA    r     | DVR-MS r    | JXL   r/w   | OFR   r     | RW2   r/w
  AAC   r     | DYLIB r     | K25   r     | OGG   r     | RWL   r/w
  AAE   r     | EIP   r     | KDC   r     | OGV   r     | RWZ   r
  AAX   r/w   | EPS   r/w   | KEY   r     | ONP   r     | RM    r
  ACR   r     | EPUB  r     | LA    r     | OPUS  r     | SEQ   r
  AFM   r     | ERF   r/w   | LFP   r     | ORF   r/w   | SKETCH r
  AI    r/w   | EXE   r     | LIF   r     | ORI   r/w   | SO    r
  AIFF  r     | EXIF  r/w/c | LNK   r     | OTF   r     | SR2   r/w
  APE   r     | EXR   r     | LRV   r/w   | PAC   r     | SRF   r
  ARQ   r/w   | EXV   r/w/c | M2TS  r     | PAGES r     | SRW   r/w
  ARW   r/w   | F4A/V r/w   | M4A/V r/w   | PBM   r/w   | SVG   r
  ASF   r     | FFF   r/w   | MACOS r     | PCAP  r     | SWF   r
  AVI   r     | FITS  r     | MAX   r     | PCAPNG r    | THM   r/w
  AVIF  r/w   | FLA   r     | MEF   r/w   | PCD   r     | TIFF  r/w
  AZW   r     | FLAC  r     | MIE   r/w/c | PCX   r     | TORRENT r
  BMP   r     | FLIF  r/w   | MIFF  r     | PDB   r     | TTC   r
  BPG   r     | FLV   r     | MKA   r     | PDF   r/w   | TTF   r
  BTF   r     | FPF   r     | MKS   r     | PEF   r/w   | TXT   r
  C2PA  r     | FPX   r     | MKV   r     | PFA   r     | VCF   r
  CHM   r     | GIF   r/w   | MNG   r/w   | PFB   r     | VNT   r
  COS   r     | GLV   r/w   | MOBI  r     | PFM   r     | VRD   r/w/c
  CR2   r/w   | GPR   r/w   | MODD  r     | PGF   r     | VSD   r
  CR3   r/w   | GZ    r     | MOI   r     | PGM   r/w   | WAV   r
  CRM   r/w   | HDP   r/w   | MOS   r/w   | PLIST r     | WDP   r/w
  CRW   r/w   | HDR   r     | MOV   r/w   | PICT  r     | WEBP  r/w
  CS1   r/w   | HEIC  r/w   | MP3   r     | PMP   r     | WEBM  r
  CSV   r     | HEIF  r/w   | MP4   r/w   | PNG   r/w   | WMA   r
  CUR   r     | HTML  r     | MPC   r     | PPM   r/w   | WMV   r
  CZI   r     | ICC   r/w/c | MPG   r     | PPT   r     | WPG   r
  DCM   r     | ICO   r     | MPO   r/w   | PPTX  r     | WTV   r
  DCP   r/w   | ICS   r     | MQV   r/w   | PS    r/w   | WV    r
  DCR   r     | IDML  r     | MRC   r     | PSB   r/w   | X3F   r/w
  DFONT r     | IIQ   r/w   | MRW   r/w   | PSD   r/w   | XCF   r
  DIVX  r     | IND   r/w   | MXF   r     | PSP   r     | XISF  r
  DJVU  r     | INSP  r/w   | NEF   r/w   | QTIF  r/w   | XLS   r
  DLL   r     | INSV  r     | NKA   r     | R3D   r     | XLSX  r
  DNG   r/w   | INX   r     | NKSC  r/w   | RA    r     | XMP   r/w/c
  DOC   r     | ISO   r     | NRW   r/w   | RAF   r/w   | ZIP   r

  Meta Information
  ----------------------+----------------------+---------------------
  EXIF           r/w/c  |  CIFF           r/w  |  Ricoh RMETA    r
  GPS            r/w/c  |  AFCP           r/w  |  Picture Info   r
  IPTC           r/w/c  |  Kodak Meta     r/w  |  Adobe APP14    r
  XMP            r/w/c  |  FotoStation    r/w  |  MPF            r
  MakerNotes     r/w/c  |  PhotoMechanic  r/w  |  Stim           r
  Photoshop IRB  r/w/c  |  JPEG 2000      r    |  DPX            r
  ICC Profile    r/w/c  |  DICOM          r    |  APE            r
  MIE            r/w/c  |  Flash          r    |  Vorbis         r
  JFIF           r/w/c  |  FlashPix       r    |  SPIFF          r
  Ducky APP12    r/w/c  |  QuickTime      r    |  DjVu           r
  PDF            r/w/c  |  Matroska       r    |  M2TS           r
  PNG            r/w/c  |  MXF            r    |  PE/COFF        r
  Canon VRD      r/w/c  |  PrintIM        r    |  AVCHD          r
  Nikon Capture  r/w/c  |  FLAC           r    |  ZIP            r
  GeoTIFF        r/w/c  |  ID3            r    |  (and more)

See html/index.html for more details about ExifTool features.

%package bin
Summary: bin components for the perl-Image-ExifTool package.
Group: Binaries

%description bin
bin components for the perl-Image-ExifTool package.


%package dev
Summary: dev components for the perl-Image-ExifTool package.
Group: Development
Requires: perl-Image-ExifTool-bin = %{version}-%{release}
Provides: perl-Image-ExifTool-devel = %{version}-%{release}
Requires: perl-Image-ExifTool = %{version}-%{release}

%description dev
dev components for the perl-Image-ExifTool package.


%package man
Summary: man components for the perl-Image-ExifTool package.
Group: Default

%description man
man components for the perl-Image-ExifTool package.


%package perl
Summary: perl components for the perl-Image-ExifTool package.
Group: Default
Requires: perl-Image-ExifTool = %{version}-%{release}

%description perl
perl components for the perl-Image-ExifTool package.


%prep
%setup -q -n Image-ExifTool-13.25
cd %{_builddir}/Image-ExifTool-13.25

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/exiftool

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::RandomAccess.3
/usr/share/man/man3/Image::ExifTool.3
/usr/share/man/man3/Image::ExifTool::7Z.3
/usr/share/man/man3/Image::ExifTool::AAC.3
/usr/share/man/man3/Image::ExifTool::AES.3
/usr/share/man/man3/Image::ExifTool::AFCP.3
/usr/share/man/man3/Image::ExifTool::AIFF.3
/usr/share/man/man3/Image::ExifTool::APE.3
/usr/share/man/man3/Image::ExifTool::APP12.3
/usr/share/man/man3/Image::ExifTool::ASF.3
/usr/share/man/man3/Image::ExifTool::Apple.3
/usr/share/man/man3/Image::ExifTool::Audible.3
/usr/share/man/man3/Image::ExifTool::BMP.3
/usr/share/man/man3/Image::ExifTool::BPG.3
/usr/share/man/man3/Image::ExifTool::BZZ.3
/usr/share/man/man3/Image::ExifTool::BigTIFF.3
/usr/share/man/man3/Image::ExifTool::BuildTagLookup.3
/usr/share/man/man3/Image::ExifTool::CBOR.3
/usr/share/man/man3/Image::ExifTool::Canon.3
/usr/share/man/man3/Image::ExifTool::CanonCustom.3
/usr/share/man/man3/Image::ExifTool::CanonRaw.3
/usr/share/man/man3/Image::ExifTool::CanonVRD.3
/usr/share/man/man3/Image::ExifTool::CaptureOne.3
/usr/share/man/man3/Image::ExifTool::Casio.3
/usr/share/man/man3/Image::ExifTool::Charset.3
/usr/share/man/man3/Image::ExifTool::DICOM.3
/usr/share/man/man3/Image::ExifTool::DJI.3
/usr/share/man/man3/Image::ExifTool::DNG.3
/usr/share/man/man3/Image::ExifTool::DPX.3
/usr/share/man/man3/Image::ExifTool::DV.3
/usr/share/man/man3/Image::ExifTool::DarwinCore.3
/usr/share/man/man3/Image::ExifTool::DjVu.3
/usr/share/man/man3/Image::ExifTool::EXE.3
/usr/share/man/man3/Image::ExifTool::Exif.3
/usr/share/man/man3/Image::ExifTool::FITS.3
/usr/share/man/man3/Image::ExifTool::FLAC.3
/usr/share/man/man3/Image::ExifTool::FLIF.3
/usr/share/man/man3/Image::ExifTool::FLIR.3
/usr/share/man/man3/Image::ExifTool::Fixup.3
/usr/share/man/man3/Image::ExifTool::Flash.3
/usr/share/man/man3/Image::ExifTool::FlashPix.3
/usr/share/man/man3/Image::ExifTool::Font.3
/usr/share/man/man3/Image::ExifTool::FotoStation.3
/usr/share/man/man3/Image::ExifTool::FujiFilm.3
/usr/share/man/man3/Image::ExifTool::GE.3
/usr/share/man/man3/Image::ExifTool::GIF.3
/usr/share/man/man3/Image::ExifTool::GIMP.3
/usr/share/man/man3/Image::ExifTool::GM.3
/usr/share/man/man3/Image::ExifTool::GPS.3
/usr/share/man/man3/Image::ExifTool::GeoTiff.3
/usr/share/man/man3/Image::ExifTool::Geolocation.3
/usr/share/man/man3/Image::ExifTool::Geotag.3
/usr/share/man/man3/Image::ExifTool::GoPro.3
/usr/share/man/man3/Image::ExifTool::H264.3
/usr/share/man/man3/Image::ExifTool::HP.3
/usr/share/man/man3/Image::ExifTool::HTML.3
/usr/share/man/man3/Image::ExifTool::HtmlDump.3
/usr/share/man/man3/Image::ExifTool::ICC_Profile.3
/usr/share/man/man3/Image::ExifTool::ICO.3
/usr/share/man/man3/Image::ExifTool::ID3.3
/usr/share/man/man3/Image::ExifTool::IPTC.3
/usr/share/man/man3/Image::ExifTool::ISO.3
/usr/share/man/man3/Image::ExifTool::ITC.3
/usr/share/man/man3/Image::ExifTool::Import.3
/usr/share/man/man3/Image::ExifTool::InDesign.3
/usr/share/man/man3/Image::ExifTool::InfiRay.3
/usr/share/man/man3/Image::ExifTool::JPEG.3
/usr/share/man/man3/Image::ExifTool::JPEGDigest.3
/usr/share/man/man3/Image::ExifTool::JSON.3
/usr/share/man/man3/Image::ExifTool::JVC.3
/usr/share/man/man3/Image::ExifTool::Jpeg2000.3
/usr/share/man/man3/Image::ExifTool::Kodak.3
/usr/share/man/man3/Image::ExifTool::KyoceraRaw.3
/usr/share/man/man3/Image::ExifTool::LIF.3
/usr/share/man/man3/Image::ExifTool::LNK.3
/usr/share/man/man3/Image::ExifTool::Lang::cs.3
/usr/share/man/man3/Image::ExifTool::Lang::de.3
/usr/share/man/man3/Image::ExifTool::Lang::en_ca.3
/usr/share/man/man3/Image::ExifTool::Lang::en_gb.3
/usr/share/man/man3/Image::ExifTool::Lang::es.3
/usr/share/man/man3/Image::ExifTool::Lang::fi.3
/usr/share/man/man3/Image::ExifTool::Lang::fr.3
/usr/share/man/man3/Image::ExifTool::Lang::it.3
/usr/share/man/man3/Image::ExifTool::Lang::ja.3
/usr/share/man/man3/Image::ExifTool::Lang::ko.3
/usr/share/man/man3/Image::ExifTool::Lang::nl.3
/usr/share/man/man3/Image::ExifTool::Lang::pl.3
/usr/share/man/man3/Image::ExifTool::Lang::ru.3
/usr/share/man/man3/Image::ExifTool::Lang::sk.3
/usr/share/man/man3/Image::ExifTool::Lang::sv.3
/usr/share/man/man3/Image::ExifTool::Lang::tr.3
/usr/share/man/man3/Image::ExifTool::Lang::zh_cn.3
/usr/share/man/man3/Image::ExifTool::Lang::zh_tw.3
/usr/share/man/man3/Image::ExifTool::Leaf.3
/usr/share/man/man3/Image::ExifTool::LigoGPS.3
/usr/share/man/man3/Image::ExifTool::Lytro.3
/usr/share/man/man3/Image::ExifTool::M2TS.3
/usr/share/man/man3/Image::ExifTool::MIE.3
/usr/share/man/man3/Image::ExifTool::MIEUnits.3
/usr/share/man/man3/Image::ExifTool::MIFF.3
/usr/share/man/man3/Image::ExifTool::MISB.3
/usr/share/man/man3/Image::ExifTool::MNG.3
/usr/share/man/man3/Image::ExifTool::MOI.3
/usr/share/man/man3/Image::ExifTool::MPC.3
/usr/share/man/man3/Image::ExifTool::MPEG.3
/usr/share/man/man3/Image::ExifTool::MPF.3
/usr/share/man/man3/Image::ExifTool::MRC.3
/usr/share/man/man3/Image::ExifTool::MWG.3
/usr/share/man/man3/Image::ExifTool::MXF.3
/usr/share/man/man3/Image::ExifTool::MacOS.3
/usr/share/man/man3/Image::ExifTool::MakerNotes.3
/usr/share/man/man3/Image::ExifTool::Matroska.3
/usr/share/man/man3/Image::ExifTool::Microsoft.3
/usr/share/man/man3/Image::ExifTool::Minolta.3
/usr/share/man/man3/Image::ExifTool::MinoltaRaw.3
/usr/share/man/man3/Image::ExifTool::Motorola.3
/usr/share/man/man3/Image::ExifTool::Nikon.3
/usr/share/man/man3/Image::ExifTool::NikonCapture.3
/usr/share/man/man3/Image::ExifTool::NikonCustom.3
/usr/share/man/man3/Image::ExifTool::NikonSettings.3
/usr/share/man/man3/Image::ExifTool::Nintendo.3
/usr/share/man/man3/Image::ExifTool::OOXML.3
/usr/share/man/man3/Image::ExifTool::Ogg.3
/usr/share/man/man3/Image::ExifTool::Olympus.3
/usr/share/man/man3/Image::ExifTool::OpenEXR.3
/usr/share/man/man3/Image::ExifTool::Opus.3
/usr/share/man/man3/Image::ExifTool::Other.3
/usr/share/man/man3/Image::ExifTool::PCAP.3
/usr/share/man/man3/Image::ExifTool::PCX.3
/usr/share/man/man3/Image::ExifTool::PDF.3
/usr/share/man/man3/Image::ExifTool::PGF.3
/usr/share/man/man3/Image::ExifTool::PICT.3
/usr/share/man/man3/Image::ExifTool::PLIST.3
/usr/share/man/man3/Image::ExifTool::PLUS.3
/usr/share/man/man3/Image::ExifTool::PNG.3
/usr/share/man/man3/Image::ExifTool::PPM.3
/usr/share/man/man3/Image::ExifTool::PSP.3
/usr/share/man/man3/Image::ExifTool::Palm.3
/usr/share/man/man3/Image::ExifTool::Panasonic.3
/usr/share/man/man3/Image::ExifTool::PanasonicRaw.3
/usr/share/man/man3/Image::ExifTool::Parrot.3
/usr/share/man/man3/Image::ExifTool::Pentax.3
/usr/share/man/man3/Image::ExifTool::PhaseOne.3
/usr/share/man/man3/Image::ExifTool::PhotoCD.3
/usr/share/man/man3/Image::ExifTool::PhotoMechanic.3
/usr/share/man/man3/Image::ExifTool::Photoshop.3
/usr/share/man/man3/Image::ExifTool::Plot.3
/usr/share/man/man3/Image::ExifTool::PostScript.3
/usr/share/man/man3/Image::ExifTool::PrintIM.3
/usr/share/man/man3/Image::ExifTool::Protobuf.3
/usr/share/man/man3/Image::ExifTool::Qualcomm.3
/usr/share/man/man3/Image::ExifTool::QuickTime.3
/usr/share/man/man3/Image::ExifTool::QuickTimeStream.3
/usr/share/man/man3/Image::ExifTool::RIFF.3
/usr/share/man/man3/Image::ExifTool::RSRC.3
/usr/share/man/man3/Image::ExifTool::RTF.3
/usr/share/man/man3/Image::ExifTool::Radiance.3
/usr/share/man/man3/Image::ExifTool::Rawzor.3
/usr/share/man/man3/Image::ExifTool::Real.3
/usr/share/man/man3/Image::ExifTool::Reconyx.3
/usr/share/man/man3/Image::ExifTool::Red.3
/usr/share/man/man3/Image::ExifTool::Ricoh.3
/usr/share/man/man3/Image::ExifTool::Samsung.3
/usr/share/man/man3/Image::ExifTool::Sanyo.3
/usr/share/man/man3/Image::ExifTool::Scalado.3
/usr/share/man/man3/Image::ExifTool::Shift.3
/usr/share/man/man3/Image::ExifTool::Shortcuts.3
/usr/share/man/man3/Image::ExifTool::Sigma.3
/usr/share/man/man3/Image::ExifTool::SigmaRaw.3
/usr/share/man/man3/Image::ExifTool::Sony.3
/usr/share/man/man3/Image::ExifTool::SonyIDC.3
/usr/share/man/man3/Image::ExifTool::Stim.3
/usr/share/man/man3/Image::ExifTool::TagInfoXML.3
/usr/share/man/man3/Image::ExifTool::TagLookup.3
/usr/share/man/man3/Image::ExifTool::TagNames.3
/usr/share/man/man3/Image::ExifTool::Text.3
/usr/share/man/man3/Image::ExifTool::Theora.3
/usr/share/man/man3/Image::ExifTool::Torrent.3
/usr/share/man/man3/Image::ExifTool::Trailer.3
/usr/share/man/man3/Image::ExifTool::Unknown.3
/usr/share/man/man3/Image::ExifTool::VCard.3
/usr/share/man/man3/Image::ExifTool::Validate.3
/usr/share/man/man3/Image::ExifTool::Vorbis.3
/usr/share/man/man3/Image::ExifTool::WPG.3
/usr/share/man/man3/Image::ExifTool::WTV.3
/usr/share/man/man3/Image::ExifTool::WriteCanonRaw.3
/usr/share/man/man3/Image::ExifTool::WriteExif.3
/usr/share/man/man3/Image::ExifTool::WriteIPTC.3
/usr/share/man/man3/Image::ExifTool::WritePDF.3
/usr/share/man/man3/Image::ExifTool::WritePNG.3
/usr/share/man/man3/Image::ExifTool::WritePhotoshop.3
/usr/share/man/man3/Image::ExifTool::WritePostScript.3
/usr/share/man/man3/Image::ExifTool::WriteQuickTime.3
/usr/share/man/man3/Image::ExifTool::WriteRIFF.3
/usr/share/man/man3/Image::ExifTool::WriteXMP.3
/usr/share/man/man3/Image::ExifTool::Writer.3
/usr/share/man/man3/Image::ExifTool::XISF.3
/usr/share/man/man3/Image::ExifTool::XMP.3
/usr/share/man/man3/Image::ExifTool::XMP2.3
/usr/share/man/man3/Image::ExifTool::XMPStruct.3
/usr/share/man/man3/Image::ExifTool::ZIP.3
/usr/share/man/man3/Image::ExifTool::ZISRAW.3
/usr/share/man/man3/Image::ExifTool::iWork.3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/exiftool.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
