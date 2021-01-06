<?php
    $name = 'Arthur Dent';

    // if ($name == 'Arthur Bent') {
    //     echo 'I could never get the hang of Thursdays.';
    // } elseif ($name == 'Marvin') {
    //     echo "I've got this terrible pain in all the diodes down my left-hand side.";
    // } else {
    //     echo 'Is that really a piece of fairy cake?';
    // }

    // $day = 'Wednesday';

    // if ($name == 'Arthur Bent' && $day == 'Thursday') {
    //     echo 'I could never get the hang of Thursdays.';
    // } elseif ($name == 'Marvin' || $day == 'Wednesday') {
    //     echo "I've got this terrible pain in all the diodes down my left-hand side.";
    // } else {
    //     echo 'Is that really a piece of fairy cake?';
    // }

    $day = 'Thursday';

    if ($name == 'Arthur Dent' && $day == 'Thursday') :
        echo 'I could never get the hang of Thursdays.';
    elseif ($name == 'Marvin' || $day == 'Wednesday') :
        echo "I've got this terrible pain in all the diodes down my left-hand side.";
    else :
        echo 'Is that really a piece of fairy cake?';
    endif;


?>