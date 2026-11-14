# The desktop editor may launch without TeX Live on PATH.
$ENV{'PATH'} = '/Library/TeX/texbin:' . $ENV{'PATH'};
$biber = '/Library/TeX/texbin/biber %O %B';
