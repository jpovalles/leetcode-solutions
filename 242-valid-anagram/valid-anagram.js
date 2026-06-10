/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
  if(s.length !== t.length) return false;
  
  let s_map = {};
  let t_map = {};
  
  for(let i = 0; i < s.length; i++){
    s_char = s[i];
    t_char = t[i];
    
    s_map[s_char] = (s_map[s_char] || 0) + 1;
    t_map[t_char] = (t_map[t_char] || 0) + 1;
  }
  
  for(let key in s_map){
    if(s_map[key] !== t_map[key]) return false
  }
  
  return true;
};