# revision 26333
# category Package
# catalog-ctan /info/latex2e-help-texinfo
# catalog-date 2012-05-10 22:36:52 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-latex2e-help-texinfo
Version:	20120510
Release:	1
Summary:	Unoffical reference manual covering LaTeX2e
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/latex2e-help-texinfo
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex2e-help-texinfo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex2e-help-texinfo.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The manual is provided as Texinfo source (which was originally
derived from the VMS help file in the DECUS TeX distribution of
1990, with many subsequent changes). This is a collaborative
development, and details of getting involved are to be found on
the package home page. All the other formats in the
distribution are derived from the Texinfo source, as usual.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/latex2e-help-texinfo/ChangeLog
%doc %{_texmfdistdir}/doc/latex/latex2e-help-texinfo/Makefile
%doc %{_texmfdistdir}/doc/latex/latex2e-help-texinfo/NEWS
%doc %{_texmfdistdir}/doc/latex/latex2e-help-texinfo/README
%doc %{_texmfdistdir}/doc/latex/latex2e-help-texinfo/latex2e.dbk
%doc %{_texmfdistdir}/doc/latex/latex2e-help-texinfo/latex2e.html
%doc %{_texmfdistdir}/doc/latex/latex2e-help-texinfo/latex2e.pdf
%doc %{_texmfdistdir}/doc/latex/latex2e-help-texinfo/latex2e.texi
%doc %{_texmfdistdir}/doc/latex/latex2e-help-texinfo/latex2e.txt
%doc %{_texmfdistdir}/doc/latex/latex2e-help-texinfo/latex2e.xml
%doc %{_texmfdistdir}/doc/latex/latex2e-help-texinfo/ltx-help.el
%doc %{_infodir}/latex2e.info*

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_infodir}
mv %{buildroot}%{_texmfdir}/doc/info/*.info %{buildroot}%{_infodir}
