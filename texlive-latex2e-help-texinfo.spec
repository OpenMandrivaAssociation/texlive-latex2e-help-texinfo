Name:		texlive-latex2e-help-texinfo
Version:	71252
Release:	1
Summary:	Unoffical reference manual covering LaTeX2e
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/latex2e-help-texinfo
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex2e-help-texinfo.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex2e-help-texinfo.doc.r%{version}.tar.xz
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
%doc %{_infodir}/latex2e.info*
%doc %{_texmfdistdir}/doc/latex/latex2e-help-texinfo

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_infodir}
mv %{buildroot}%{_texmfdistdir}/doc/info/*.info %{buildroot}%{_infodir}
