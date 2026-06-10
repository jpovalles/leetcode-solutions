/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
var wordPattern = function(pattern, s) {
  let ans = false;
  let words = s.split(' ');
  
  if(pattern.length === words.length){
    let map_to_s = {};
    let map_to_p = {};
    
    for(let i = 0; i < pattern.length; i++){
      let char_p = pattern[i];
      let w = words[i];

      if(map_to_s.hasOwnProperty(char_p)){
        if(map_to_s[char_p] !== w) return false
      }else if(map_to_p.hasOwnProperty(w)){
        if(map_to_p[w] !== char_p) return false
      }else{
        map_to_s[char_p] = w;
        map_to_p[w] = char_p;
      }
    }
    ans = true;
  }
  return ans;
};