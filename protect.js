(function(){
  // Basic deterrents only — not real security. Anyone who knows dev tools
  // can still view source via the network tab. This just raises casual friction.

  document.addEventListener('contextmenu', function(e){ e.preventDefault(); });

  document.addEventListener('keydown', function(e){
    var k = e.key;
    var blockCombo = e.ctrlKey && e.shiftKey && (k === 'I' || k === 'J' || k === 'C');
    var blockViewSource = e.ctrlKey && k === 'u';
    var blockF12 = k === 'F12';
    if (blockCombo || blockViewSource || blockF12) {
      e.preventDefault();
    }
  });

  console.log('%cStop.', 'color:#FF7A00; font-size:42px; font-weight:800;');
  console.log("%cThis console is for developers. Pasting code here on someone else's instruction can compromise your accounts. If you didn't come here on purpose, close this tab.", 'font-size:14px; color:#5B6478;');
})();
