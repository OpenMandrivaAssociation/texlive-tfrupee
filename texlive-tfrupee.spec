# revision 20770
# category Package
# catalog-ctan /fonts/tfrupee
# catalog-date 2010-12-16 15:42:40 +0100
# catalog-license gpl3
# catalog-version 1.02
Name:		texlive-tfrupee
Version:	1.02
Release:	11
Summary:	A font offering the new (Indian) Rupee symbol
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/tfrupee
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tfrupee.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tfrupee.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tfrupee.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%define		_unpackaged_subdirs_terminate_build	0

%description
The package provides LaTeX support for the (Indian) Rupee
symbol font, created by TechFat. The original font has been
converted to Adobe Type 1 format, and simple LaTeX support
written for its use.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/tfrupee/tfrupee.afm
%{_texmfdistdir}/fonts/map/dvips/tfrupee/tfrupee.map
%{_texmfdistdir}/fonts/tfm/public/tfrupee/tfrupee.tfm
%{_texmfdistdir}/fonts/type1/public/tfrupee/tfrupee.pfb
%{_texmfdistdir}/tex/latex/tfrupee/tfrupee.sty
%doc %{_texmfdistdir}/doc/fonts/tfrupee/LICENSE
%doc %{_texmfdistdir}/doc/fonts/tfrupee/README
%doc %{_texmfdistdir}/doc/fonts/tfrupee/tfrupee.pdf
%doc %{_texmfdistdir}/doc/fonts/tfrupee/tfrupee.tex
#- source
%doc %{_texmfdistdir}/source/fonts/tfrupee/tfrupee.sfd

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.02-2
+ Revision: 756832
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.02-1
+ Revision: 719724
- texlive-tfrupee
- texlive-tfrupee
- texlive-tfrupee

