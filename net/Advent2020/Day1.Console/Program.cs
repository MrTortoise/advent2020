using System;
using System.IO;
using System.Linq;
using System.Net.Http;
using System.Threading.Tasks;
using Day1.Spec;

namespace Day1.Console
{
    class Program
    {
        static async Task Main(string[] args)
        {
            var client = new HttpClient();
            var data = await File.ReadAllLinesAsync("data.txt");
            var solver = new Solver();
            System.Console.WriteLine(solver.Solve3(data.Select(int.Parse)));

            System.Console.ReadLine();
        }
    }
}
