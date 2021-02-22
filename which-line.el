;; which-line.el file

(defun which-line ()
  "Print the current line (in the buffer) of point"
  (interactive)
  (save-restriction
    (widen)
    (save-excursion
      (beginning-of-line)
      (message "Line %d of %d" ;; message that takes in values
               (1+ (count-lines 1 (point)))  ;; current line value

	       ;; if statement to determine whether last line is new line or not
	       (if (/= 10 (char-before (point-max)))
                   (1+ (- 1 (count-lines 1 (point-max)))) ;; -1 if new line
                   (1+ (count-lines 1 (point-max)))       ;; no change if no new line
                   )
                                     
	       ))))
