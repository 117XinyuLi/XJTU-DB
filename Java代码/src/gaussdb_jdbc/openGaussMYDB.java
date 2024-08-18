package src.gaussdb_jdbc;

import java.io.BufferedReader;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import java.io.FileReader;
import java.util.concurrent.TimeUnit;

public class openGaussMYDB {

    static final String JDBC_DRIVER = "org.postgresql.Driver";
    static final String DB_URL = "jdbc:postgresql://192.168.150.134:7654/mydb";
    // 数据库的用户名与密码，需要根据自己的设置
    static final String USER = "testuser";
    static final String PASS = "A1a2a3a4a5$";


    public static void ExecSQL(Connection conn, String filename) throws IOException,
            InterruptedException {
        FileReader fr=new FileReader(filename);
        BufferedReader br=new BufferedReader(fr);
        String line;
        String buffer="";
        while ((line=br.readLine())!=null) {
            if (!line.contains("--")){
                buffer = buffer + line + " ";
            }
            if (line.contains(";")){
                // 执行sql语句
                // System.out.println("Executing: " + buffer);
                if (buffer.contains("INSERT")){
                    System.out.println("SQL: INSERT");
                }
                if (buffer.contains("DELETE")){
                    System.out.println("SQL: DELETE");
                }
                Statement stmt = null;
                try {
                    stmt = conn.createStatement();
                    stmt.execute(buffer);
                    stmt.close();
                    TimeUnit.MICROSECONDS.sleep(1000);
                } catch (SQLException e) {
                    System.out.println("Error occurs when executing " + buffer);
                    if (stmt != null) {
                        try {
                            stmt.close();
                        } catch (SQLException e1) {
                            e1.printStackTrace();
                        }
                    }
                    e.printStackTrace();
                }
                buffer = "";
            }
        }
        br.close();
        fr.close();
    }

    public static void testSQL(Connection conn){
        try{
            // 执行查询
            System.out.println(" 实例化Statement对象...");
            Statement stmt = conn.createStatement();
            String sql;
            sql = "SELECT * FROM sc049";
            ResultSet rs = stmt.executeQuery(sql);

            int count = 0;
            // 展开结果集数据库
            while(rs.next()){
                // 通过字段检索
                String Sno  = rs.getString("Sno");
                String Cno = rs.getString("Cno");
                String Grade = rs.getString("Grade");


                // 输出数据
                System.out.print("Sno: " + Sno);
                System.out.print(", Cno: " + Cno);
                System.out.print(", Grade: " + Grade);
                System.out.print("\n");

                count++;
            }
            // 完成后关闭
            rs.close();
            stmt.close();
            System.out.println("Total: " + count);

        }catch(SQLException se){
            // 处理 JDBC 错误
            se.printStackTrace();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void ExecSQL_Times(Connection conn, String filename, Integer lines) throws IOException,
            InterruptedException {
        // 读取1000行就执行一次SQL
        FileReader fr=new FileReader(filename);
        BufferedReader br=new BufferedReader(fr);
        String line;
        String buffer="";
        int line_count = 0;
        String first_line = "";
        // 读入第一行，为SQL语句的第一部分
        if ((line=br.readLine())!=null) {
            first_line = line;
        }
        // 每1000行执行一次SQL
        buffer = first_line;
        while ((line=br.readLine())!=null) {
            if (!line.contains("--")){
                buffer = buffer + line + " ";
                line_count++;
            }
            if (line_count == lines || line.contains(";")){
                line_count = 0;
                // 将buffer中的最后一个字符设置为';'
                buffer = buffer.substring(0, buffer.length() - 2) + ";";
                // 执行sql语句
                System.out.println("Executing: " + buffer);

                Statement stmt = null;
                try {
                    stmt = conn.createStatement();
                    stmt.execute(buffer);
                    stmt.close();
                    TimeUnit.MICROSECONDS.sleep(1000);
                } catch (SQLException e) {
                    System.out.println("Error occurs when executing " + buffer);
                    if (stmt != null) {
                        try {
                            stmt.close();
                        } catch (SQLException e1) {
                            e1.printStackTrace();
                        }
                    }
                    e.printStackTrace();
                }

                buffer = first_line;
            }


        }

        br.close();
        fr.close();
    }

    public static void main(String[] args) {
        Connection conn = null;
        try{
            // 注册 JDBC 驱动
            Class.forName(JDBC_DRIVER);

            // 打开链接
            System.out.println("连接数据库...");
            conn = DriverManager.getConnection(DB_URL,USER,PASS);

            // 测试SQL
            testSQL(conn);

            // 读入S049_1.txt文件并执行sql语句
            // ExecSQL(conn, "./scripts/S049_1.txt");

            // 读入C049_1.txt文件并执行sql语句
            // ExecSQL(conn, "./scripts/C049_1.txt");

            /*
            // 并行执行SC049_1.txt文件中的和delete_less_than_60.txt文件中的sql语句
            Connection finalConn = conn;
            Thread t1 = new Thread(new Runnable() {
                @Override
                public void run() {
                    try {
                        ExecSQL_Times(finalConn, "./scripts/SC049_1.txt", 100);
                    } catch (IOException | InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            });

            Thread t2 = new Thread(new Runnable() {
                @Override
                public void run() {
                    try {
                        TimeUnit.SECONDS.sleep(2);
                        ExecSQL(finalConn, "./scripts/delete_less_than_60.txt");
                    } catch (IOException | InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            });

            t1.start();
            t2.start();

            t1.join();
            t2.join();
            */

            // 读入S049_2.txt文件并执行sql语句
            // ExecSQL(conn, "./scripts/S049_2.txt");

            // 读入C049_2.txt文件并执行sql语句
            // ExecSQL(conn, "./scripts/C049_2.txt");

            // 读入SC049_2.txt文件并执行sql语句
            // ExecSQL(conn, "./scripts/SC049_2.txt");


            conn.close();

        }catch(SQLException se){
            // 处理 JDBC 错误
            se.printStackTrace();
        }catch(Exception e){
            // 处理 Class.forName 错误
            e.printStackTrace();
        }
    }
}
