title: PHP 屏蔽特殊符号
date: 2013-03-20 11:50:02
tags: PHP
categories: PHP
---

用户注册用户名的时候往往会带有一些特殊符号，因为特殊要求，需要对特殊符号和屏蔽字进行处理。

网上说的方案都以正则为基础，进行匹配过滤。都不太适用。

<!-- more -->

    <?php

    class Blacklist {

        //保留的
        private static $keywords_reserved = array ('官方', '内幕消息', '管理员', '版主', '客服',);
        
        //保留的追加
        private static $keywords_reserved_exact = array ('mem','vip','account', 'admin');

        //严格
        public static $keywords_strict = array ('时代论坛');

        //丢失
        private static $keywords_loose = array ();

        //屏蔽
        private static $keywords_forbidden = array('爱梦');
        
        /*
            是否有关键词
         */
        public static function has_blackword($content) {
            if (self::has_blackword_strict ( $content ))
                return true;
            if (self::has_blackword_loose ( $content ))
                return true;
            return false;
        }
        
        public static function has_blackword_strict($content) {
            foreach ( self::$keywords_strict as $blackword ) {
                if (strpos ( $content, $blackword ) !== false) {
                    return true;
                }
            }
            return false;
        }
        
        /*
            是否有屏蔽的关键词
         */
        public static function has_forbiddenword($content) {
            global $auth;
            if (is_object($auth) && $auth->is_logged_in() && $auth->id == 7878) {
                return false;
            }
            if (self::has_forbiddenword_loose($content))
                return true;
            return false;
        }
        
        public static function has_forbiddenword_loose($content) {
            $pure_content = self::get_purewords($content);
            
            if (preg_match('/q[0-9]{10,}/i', $pure_content)) {
                return true;
            }
            if (/*strpos($content, '电话') ||  */strpos($content, '来电') || strpos($content, '号码') 
             || strpos($content, '致电') || strpos($content, '热线') 
             /*|| stripos($content, 'tel')*/) {
                if (preg_match('/[0-9]{10,11}/i', $pure_content)) {
                    return true;
                }
            }
        
            //do somethings
            
            return false;
        }
        
        public static function has_blackword_loose($content) {
            foreach ( self::$keywords_loose as $blackword ) {
                if (strpos ( $content, $blackword ) !== false) {
                    return true;
                }
            }
            return false;
        }
        
        public static function has_reserved_word($content) {
            $content = trim ( $content );
            foreach ( self::$keywords_reserved as $word ) {
                if (stripos ( $content, $word ) !== false) {
                    return true;
                }
            }
            foreach ( self::$keywords_reserved_exact as $word ) {
                if ($content == $word)
                    return true;
            }
            return false;
        }
        
        public static function replace_blackwords_strict($content, $replace = '*') {
            $content = str_replace ( self::$keywords_strict, $replace, $content );
            return $content;
        }
        
        public static function replace_blackwords_loose($content, $replace = '*') {
            $content = str_replace ( self::$keywords_loose, $replace, $content );
            return $content;
        }
        
        private static $marks = array('<br>','&nbsp;',' ','-','－', '.', '。','×','┆',
                                    ',','，','●','○' ,':','◆','━','*','、','※','Ж',
                                    '★','☆','卐','┼','〓','【','】','[',']','█','▂',
                                    '&','%','　','!','~','：','▓','…','┠','┨','◢',
                                    '|','？','◣','；','(',')','（','）','《','》','╮',
                                    '╰','！','“','”','=','∏','＠','@','┗','┛','√',
                                    '‖','+','{','≯','/','╉','_','→','〖','べ','〗');
        private static $SBCcase = array('０' => 0,
                                        '零' => 0,
                                        '１' => 1,
                                        '①' => 1,
                                        '壹' => 1,
                                        '一' => 1,
                                        '㈠' => 1,
                                        '⒈' => 1,
                                        '⑴' => 1,
                                        '２' => 2,
                                        '②' => 2,
                                        '二' => 2, 
                                        '贰' => 2, 
                                        '⑵' => 2,
                                        '㈡' => 2,
                                        '⒉' => 2,
                                        '３' => 3,
                                        '③' => 3,
                                        '三' => 3,
                                        '㈢' => 3,
                                        '⑶' => 3,
                                        '⒊' => 3,
                                        '叁' => 3,
                                        '４' => 4, 
                                        '④' => 4, 
                                        '四' => 4, 
                                        '㈣' => 4, 
                                        '⑷' => 4, 
                                        '⒋' => 4, 
                                        '肆' => 4, 
                                        '５' => 5,
                                        '㈤' => 5,
                                        '㈤' => 5,
                                        '⑸' => 5,
                                        '⒌' => 5,
                                        '⑤' => 5,
                                        '五' => 5,
                                        '伍' => 5,
                                        '６' => 6,
                                        '⒍' => 6,
                                        '⑹' => 6,
                                        '㈥' => 6,
                                        '⑥' => 6,
                                        '六' => 6,
                                        '陸' => 6,
                                        '７' => 7,
                                        '㈦' => 7,
                                        '㈦' => 7,
                                        '⑺' => 7,
                                        '⒎' => 7,
                                        '⑦' => 7,
                                        '七' => 7,
                                        '柒' => 7,
                                        '８' => 8,
                                        '㈧' => 8,
                                        '⑻' => 8,
                                        '⒏' => 8,
                                        '⑧' => 8,
                                        '八' => 8,
                                        '捌' => 8,
                                        '９' => 9,
                                        '㈨' => 9,
                                        '⑼' => 9,
                                        '⑼' => 9,
                                        '⒐' => 9,
                                        '⑨' => 9,
                                        '九' => 9,
                                        '玖' => 9,
                                        '⑩' => 10,
                                        '㈩' => 10,
                                        '⑽' => 10,
                                        '⒑' => 10,
                                        '⑾' => 11,
                                        '⒒' => 11,
                                        '⑿' => 12,
                                        '⒓' => 12,
                                        '⒀' => 13,
                                        '⒔' => 13,
                                        '⒁' => 14,
                                        '⒕' => 14,
                                        '⒂' => 15,
                                        '⒖' => 15,
                                        '⒃' => 16,
                                        '⒗' => 16,
                                        '⒄' => 17,
                                        '⒘' => 17,
                                        '⒅' => 18,
                                        '⒙' => 18,
                                        '⒆' => 19,
                                        '⒚' => 19,
                                        '⒇' => 20,
                                        '⒛' => 20,
                                        'Ａ' =>'a',
                                        'Ｂ' =>'b',
                                        'Ｃ' =>'c',
                                        'Ｄ' =>'d',
                                        'Ｅ' =>'e',
                                        'Ｆ' =>'f',
                                        'Ｇ' =>'g',
                                        'Ｈ' =>'h',
                                        'Ｉ' =>'i',
                                        'Ｊ' =>'j',
                                        'Ｋ' =>'k',
                                        'Ｌ' =>'l',
                                        'Ｍ' =>'m',
                                        'Ｎ' =>'n',
                                        'Ｏ' =>'o',
                                        'Ｐ' =>'p',
                                        'Ｑ' =>'q',
                                        'Ｒ' =>'r',
                                        'Ｓ' =>'s',
                                        'Ｔ' =>'t',
                                        'Ｕ' =>'u',
                                        'Ｖ' =>'v',
                                        'Ｗ' =>'w',
                                        'Ｘ' =>'x',
                                        'Ｙ' =>'y',
                                        'Ｚ' =>'z',
                                        'ａ' =>'a',
                                        'ｂ' =>'b',
                                        'ｃ' =>'c',
                                        'ｄ' =>'d',
                                        'ｅ' =>'e',
                                        'ｆ' =>'f',
                                        'ｇ' =>'g',
                                        'ｈ' =>'h',
                                        'ｉ' =>'i',
                                        'ｊ' =>'j',
                                        'ｋ' =>'k',
                                        'ｌ' =>'l',
                                        'ｍ' =>'m',
                                        'ｎ' =>'n',
                                        'ｏ' =>'o',
                                        'ｐ' =>'p',
                                        'ｑ' =>'q',
                                        'ｒ' =>'r',
                                        'ｓ' =>'s',
                                        'ｔ' =>'t',
                                        'ｕ' =>'u',
                                        'ｖ' =>'v',
                                        'ｗ' =>'w',
                                        'ｘ' =>'x',
                                        'ｙ' =>'y',
                                        'ｚ' =>'z',
                                        '℡' => 'TEL');                                  
        public static function get_purewords($content) {
            $content = str_replace(self::$marks, '', $content);
            $content = strip_tags($content);
            foreach (self::$SBCcase as $key => $value) {
                $content = str_replace($key, $value, $content);
            }
            $content = preg_replace("/[^\x{4e00}-\x{9fa5}a-z0-9]/iu", '', $content);
            return $content;
        }
        
        //api接口注册，替换不合法符号
        public static function get_pure_nickname($content) {
            $keywords = array_merge(self::$keywords_reserved, self::$keywords_reserved_exact, self::$keywords_forbidden, self::$keywords_loose, self::$keywords_strict);
            $keywords_replace = array();
            foreach ($keywords as $k => $v) {
                $keywords_replace [$v] = '';
            }
            $content = strtr($content, $keywords_replace);
            
            $content = self::get_purewords($content);
            
            return $content;
        }
    }
    ?>
