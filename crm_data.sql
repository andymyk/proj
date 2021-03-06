PGDMP     /    +                y           data    13.4    13.4     ?           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ?           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ?           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            ?           1262    24576    data    DATABASE     d   CREATE DATABASE data WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Ukrainian_Ukraine.1251';
    DROP DATABASE data;
                postgres    false            ?            1259    24646    clients    TABLE     _   CREATE TABLE public.clients (
    client_id integer,
    telegram_usr character varying(50)
);
    DROP TABLE public.clients;
       public         heap    postgres    false            ?            1259    24619    departments    TABLE     k   CREATE TABLE public.departments (
    department_id integer,
    department_name character varying(100)
);
    DROP TABLE public.departments;
       public         heap    postgres    false            ?            1259    24616 	   employees    TABLE     ?   CREATE TABLE public.employees (
    employee_id integer,
    personal_data character varying(100),
    job_position character varying(100),
    department_id integer
);
    DROP TABLE public.employees;
       public         heap    postgres    false            ?            1259    24607    orders    TABLE     :  CREATE TABLE public.orders (
    order_id integer NOT NULL,
    created_dt character varying,
    updated_dt character varying,
    order_type character varying(100),
    description character varying(300),
    status character varying(100),
    serial_no integer,
    creator_id integer,
    client_id integer
);
    DROP TABLE public.orders;
       public         heap    postgres    false            ?            1259    24605    orders_order_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.orders_order_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.orders_order_id_seq;
       public          postgres    false    201            ?           0    0    orders_order_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.orders_order_id_seq OWNED BY public.orders.order_id;
          public          postgres    false    200            ?            1259    24625    subscribers    TABLE     ?   CREATE TABLE public.subscribers (
    username character varying(30) NOT NULL,
    is_subscribed character varying(30) NOT NULL
);
    DROP TABLE public.subscribers;
       public         heap    postgres    false            3           2604    24610    orders order_id    DEFAULT     r   ALTER TABLE ONLY public.orders ALTER COLUMN order_id SET DEFAULT nextval('public.orders_order_id_seq'::regclass);
 >   ALTER TABLE public.orders ALTER COLUMN order_id DROP DEFAULT;
       public          postgres    false    200    201    201            ?          0    24646    clients 
   TABLE DATA           :   COPY public.clients (client_id, telegram_usr) FROM stdin;
    public          postgres    false    205   c       ?          0    24619    departments 
   TABLE DATA           E   COPY public.departments (department_id, department_name) FROM stdin;
    public          postgres    false    203   ?       ?          0    24616 	   employees 
   TABLE DATA           \   COPY public.employees (employee_id, personal_data, job_position, department_id) FROM stdin;
    public          postgres    false    202   ?       ?          0    24607    orders 
   TABLE DATA           ?   COPY public.orders (order_id, created_dt, updated_dt, order_type, description, status, serial_no, creator_id, client_id) FROM stdin;
    public          postgres    false    201   p       ?          0    24625    subscribers 
   TABLE DATA           >   COPY public.subscribers (username, is_subscribed) FROM stdin;
    public          postgres    false    204   ?       ?           0    0    orders_order_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.orders_order_id_seq', 1, false);
          public          postgres    false    200            5           2606    24615    orders orders_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (order_id);
 <   ALTER TABLE ONLY public.orders DROP CONSTRAINT orders_pkey;
       public            postgres    false    201            ?   J   x?E?)?@DA?????.?q???ϕ+???۟r4GK?F[?GGtF?? ?xD$&Q?Kdb3???f?k???YN{      ?   r   x?340??0???.l???b???
?]l???b#???)煅@??@??b??&??1??ypy#?/6_l???j?Ŧ[/6 ???R&??\?4,x???Ș??<??+F??? ?Q??      ?   !  x?uQKN?P\???? ??-??p?4?j???*T?Q?H!(?
??y????Ο?g<?Ԛi???&?{4V??j??
a\"?A?ul|???F)x7???<vC?
????h?	??"???n$x@????q???n???Z1тg???????V[?HQx,5?S??V񪔇??T??̶?}???>c?P?9}?I???|????L???r?ZC?،???딓?!?u4q!??E?*^?sZ`?????GPr????f?P#?]+???|??_???<q?? ??O*      ?   	  x???Ar?0E??)zw???u?tY?:i3]t?8?n??\?I?Ʊ??
??
@?Dg??m?3?94?@????0??=ʐ?!??5/x?/? O?N^???????R&??%7?2]تF?W?p?|?>?? )?҉jB?@?? R??o???I?i.z?t?~?2ݹ??n????rë4契ekpd?!׃z?^?f??[Et?r?O?l?iA?k?"??M??(?F??<?%DE8????J??II???49??T?\??F??$?Z?jW??IH??R1??V??غ?S??*?Vx?????yi-,?=K??????rNB?a?,?x,w?8??HJ	?????S?C???o???~?b??;X̝0E???\vza
??kIv?ja0?u ?[&nO*??:?&!n??yl?FD1O2?V?AX????~ӫ-?e93??$??C8?R;??ƼG`y?	?????!Io??γ????;חmҕ??C[??sn1?v???7G?H?O?O?5Z?      ?   C   x??????)*M???L?HĹp\???K2R!??Ԓ?"?=5?(=????,??;??TBX1z\\\ ?\     